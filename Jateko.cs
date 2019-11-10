using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace roglecke2
{
    class Jateko
    {
        
        string neve="default name";
        int kill =0;
        int death = 0;


        public Jateko(string neve)
        {
            this.neve = neve;
        }

        public string get()
        {
            return neve;
        }

        





        public void gyilkolas()
        {
            kill++;
        }

        public void halalozas()
        {
            death++;
        }

        public double kd()
        {
            if(death==0)
            {
                return kill;
            }

            return (double)kill / (double)death;
        }

        public string ToString()
        {
            return neve + " k/d:" + kd() + " .";
        }
        
    }
}
