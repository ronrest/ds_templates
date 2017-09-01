"""
GENERIC template for performing training operation for n_epochs
"""

# global_epoch=0
#
# def evaluate()
#
# evals = {}
# evals["train_acc"] = []
# evals["train_loss"] = []
# evals["valid_acc"] = []
# evals["valid_loss"] = []


def train(data, n_epochs, batch_size, print_every):
    alpha = 0.01
    n_samples = len(data["X_train"])               # Num training samples
    n_batches = int(np.ceil(n_samples/batch_size)) # Num batches per epoch

    t0 = time.time()
    try:
        for epoch in range(1, n_epochs+1):
            global_epoch += 1
            print("="*70, "\nEPOCH {}/{} (GLOBAL_EPOCH: {})".format(epoch, n_epochs, global_epoch),"\n"+("="*70))

            # Shuffle the data
            permutation = list(np.random.permutation(n_samples))
            data["X_train"] = data["X_train"][permutation]
            data["Y_train"] = data["Y_train"][permutation]

            # Iterate through each mini-batch
            for i in range(n_batches):
                Xbatch = data["X_train"][batch_size*i: batch_size*(i+1)]
                Ybatch = data["Y_train"][batch_size*i: batch_size*(i+1)]

                #----------------------
                # BOOKMARK: Train steps
                #----------------------
                loss = train_step()

                # Print feedback every so often
                if i%print_every==0:
                    print("{}    Batch_loss: {}".format(pretty_time(time.time()-t0), loss))

            # BOOKMARK: Save parameters after each epoch
            # save

            # Evaluate on full train and validation sets after each epoch
            # BOOKMARK: evaluate function api
            train_acc, train_loss = evaluate(data["X_train"], data["Y_train"])
            valid_acc, valid_loss = evaluate(data["X_valid"], data["Y_valid"])
            evals["train_acc"].append(train_acc)
            evals["train_loss"].append(train_loss)
            evals["valid_acc"].append(valid_acc)
            evals["valid_loss"].append(valid_loss)

            # Print evaluations
            s = "\nTR ACC: {: 3.3f} VA ACC: {: 3.3f} TR LOSS: {: 3.5f} VA LOSS: {: 3.5f}\n"
            print(s.format(train_acc, valid_acc, train_loss, valid_loss))

    except KeyboardInterrupt as e:
        print("Keyboard interupt detected. Exiting gracefully")
        # BOOKMARK: Fall gracefully
        raise e
