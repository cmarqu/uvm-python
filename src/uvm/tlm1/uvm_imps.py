#//
#//------------------------------------------------------------------------------
#//   Copyright 2007-2011 Mentor Graphics Corporation
#//   Copyright 2007-2010 Cadence Design Systems, Inc.
#//   Copyright 2010 Synopsys, Inc.
#//   All Rights Reserved Worldwide
#//
#//   Licensed under the Apache License, Version 2.0 (the
#//   "License"); you may not use this file except in
#//   compliance with the License.  You may obtain a copy of
#//   the License at
#//
#//       http://www.apache.org/licenses/LICENSE-2.0
#//
#//   Unless required by applicable law or agreed to in
#//   writing, software distributed under the License is
#//   distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
#//   CONDITIONS OF ANY KIND, either express or implied.  See
#//   the License for the specific language governing
#//   permissions and limitations under the License.
#//-------------.----------------------------------------------------------------

#//------------------------------------------------------------------------------
#// Title: uvm_*_imp ports
#//
#// The following defines the TLM implementation (imp) classes.
#//------------------------------------------------------------------------------

from .uvm_tlm_imps import (UVM_BLOCKING_GET_IMP, UVM_BLOCKING_GET_PEEK_IMP, UVM_BLOCKING_PEEK_IMP,
                           UVM_BLOCKING_PUT_IMP, UVM_BLOCKING_TRANSPORT_IMP, UVM_GET_IMP,
                           UVM_GET_PEEK_IMP, UVM_IMP_COMMON, UVM_MS_IMP_COMMON,
                           UVM_NONBLOCKING_GET_IMP, UVM_NONBLOCKING_GET_PEEK_IMP,
                           UVM_NONBLOCKING_PEEK_IMP, UVM_NONBLOCKING_PUT_IMP,
                           UVM_NONBLOCKING_TRANSPORT_IMP, UVM_PEEK_IMP, UVM_PUT_IMP)
from ..base.uvm_port_base import UVMPortBase
from ..macros.uvm_tlm_defines import (UVM_TLM_BLOCKING_GET_MASK, UVM_TLM_BLOCKING_GET_PEEK_MASK,
                                      UVM_TLM_BLOCKING_MASTER_MASK, UVM_TLM_BLOCKING_PEEK_MASK,
                                      UVM_TLM_BLOCKING_PUT_MASK, UVM_TLM_BLOCKING_SLAVE_MASK,
                                      UVM_TLM_BLOCKING_TRANSPORT_MASK, UVM_TLM_GET_MASK,
                                      UVM_TLM_GET_PEEK_MASK, UVM_TLM_MASTER_MASK,
                                      UVM_TLM_NONBLOCKING_GET_MASK,
                                      UVM_TLM_NONBLOCKING_GET_PEEK_MASK,
                                      UVM_TLM_NONBLOCKING_MASTER_MASK,
                                      UVM_TLM_NONBLOCKING_PEEK_MASK, UVM_TLM_NONBLOCKING_PUT_MASK,
                                      UVM_TLM_NONBLOCKING_SLAVE_MASK,
                                      UVM_TLM_NONBLOCKING_TRANSPORT_MASK, UVM_TLM_PEEK_MASK,
                                      UVM_TLM_PUT_MASK, UVM_TLM_SLAVE_MASK, UVM_TLM_TRANSPORT_MASK)

#//------------------------------------------------------------------------------
#//
#// CLASS: uvm_*_imp #(T,IMP)
#//
#// Unidirectional implementation (imp) port classes--An imp port provides access
#// to an implementation of the associated interface to all connected ~ports~ and
#// ~exports~. Each imp port instance ~must~ be connected to the component instance
#// that implements the associated interface, typically the imp port's parent.
#// All other connections-- e.g. to other ports and exports-- are prohibited.
#//
#// The asterisk in ~uvm_*_imp~ may be any of the following
#//
#//|  blocking_put
#//|  nonblocking_put
#//|  put
#//|
#//|  blocking_get
#//|  nonblocking_get
#//|  get
#//|
#//|  blocking_peek
#//|  nonblocking_peek
#//|  peek
#//|
#//|  blocking_get_peek
#//|  nonblocking_get_peek
#//|  get_peek
#//
#// Type parameters
#//
#// T   - The type of transaction to be communicated by the imp
#//
#// IMP - The type of the component implementing the interface. That is, the class
#//       to which this imp will delegate.
#//
#// The interface methods are implemented in a component of type ~IMP~, a handle
#// to which is passed in a constructor argument.  The imp port delegates all
#// interface calls to this component.
#//
#//------------------------------------------------------------------------------


#// Function: new
#//
#// Creates a new unidirectional imp port with the given ~name~ and ~parent~.
#// The ~parent~ must implement the interface associated with this port.
#// Its type must be the type specified in the imp's type-parameter, ~IMP~.
#//
#//|  function new (string name, IMP parent);

#class uvm_blocking_put_imp #(type T=int, type IMP=int)
#  extends uvm_port_base #(uvm_tlm_if_base #(T,T));
#  `UVM_IMP_COMMON(`UVM_TLM_BLOCKING_PUT_MASK,"uvm_blocking_put_imp",IMP)
#  `UVM_BLOCKING_PUT_IMP (m_imp, T, t)
#endclass
class UVMBlockingPutImp():
    pass
UVMBlockingPutImp = UVM_IMP_COMMON(UVMBlockingPutImp, UVM_TLM_BLOCKING_PUT_MASK, "uvm_blocking_put_imp")
UVM_BLOCKING_PUT_IMP('m_imp', UVMBlockingPutImp)

#class uvm_nonblocking_put_imp #(type T=int, type IMP=int)
#  extends uvm_port_base #(uvm_tlm_if_base #(T,T));
#  `UVM_IMP_COMMON(`UVM_TLM_NONBLOCKING_PUT_MASK,"uvm_nonblocking_put_imp",IMP)
#  `UVM_NONBLOCKING_PUT_IMP (m_imp, T, t)
#endclass
class UVMNonBlockingPutImp():
    pass
UVMNonBlockingPutImp = UVM_IMP_COMMON(UVMNonBlockingPutImp, UVM_TLM_NONBLOCKING_PUT_MASK, "uvm_nonblocking_put_imp")
UVM_NONBLOCKING_PUT_IMP('m_imp', UVMNonBlockingPutImp)

#class uvm_put_imp #(type T=int, type IMP=int)
#  extends uvm_port_base #(uvm_tlm_if_base #(T,T));
#  `UVM_IMP_COMMON(`UVM_TLM_PUT_MASK,"uvm_put_imp",IMP)
#  `UVM_PUT_IMP (m_imp, T, t)
#endclass
class UVMPutImp():
    pass
UVMPutImp = UVM_IMP_COMMON(UVMPutImp, UVM_TLM_PUT_MASK,"uvm_put_imp")
UVM_PUT_IMP('m_imp', UVMPutImp)

#class uvm_blocking_get_imp #(type T=int, type IMP=int)
#  extends uvm_port_base #(uvm_tlm_if_base #(T,T));
#  `UVM_IMP_COMMON(`UVM_TLM_BLOCKING_GET_MASK,"uvm_blocking_get_imp",IMP)
#  `UVM_BLOCKING_GET_IMP (m_imp, T, t)
#endclass
class UVMBlockingGetImp():
    pass
UVMBlockingGetImp = UVM_IMP_COMMON(UVMBlockingGetImp, UVM_TLM_BLOCKING_GET_MASK,"uvm_blocking_get_imp")
UVM_BLOCKING_GET_IMP('m_imp', UVMBlockingGetImp)

#class uvm_nonblocking_get_imp #(type T=int, type IMP=int)
#  extends uvm_port_base #(uvm_tlm_if_base #(T,T));
#  `UVM_IMP_COMMON(`UVM_TLM_NONBLOCKING_GET_MASK,"uvm_nonblocking_get_imp",IMP)
#  `UVM_NONBLOCKING_GET_IMP (m_imp, T, t)
#endclass
class UVMNonBlockingGetImp():
    pass
UVMNonBlockingGetImp = UVM_IMP_COMMON(UVMNonBlockingGetImp, UVM_TLM_NONBLOCKING_GET_MASK,"uvm_nonblocking_get_imp")
UVM_NONBLOCKING_GET_IMP('m_imp', UVMNonBlockingGetImp)

#class uvm_get_imp #(type T=int, type IMP=int)
#  extends uvm_port_base #(uvm_tlm_if_base #(T,T));
#  `UVM_IMP_COMMON(`UVM_TLM_GET_MASK,"uvm_get_imp",IMP)
#  `UVM_GET_IMP (m_imp, T, t)
#endclass
class UVMGetImp():
    pass
UVMGetImp = UVM_IMP_COMMON(UVMGetImp, UVM_TLM_GET_MASK,"uvm_get_imp")
UVM_GET_IMP('m_imp', UVMGetImp)

#class uvm_blocking_peek_imp #(type T=int, type IMP=int)
#  extends uvm_port_base #(uvm_tlm_if_base #(T,T));
#  `UVM_IMP_COMMON(`UVM_TLM_BLOCKING_PEEK_MASK,"uvm_blocking_peek_imp",IMP)
#  `UVM_BLOCKING_PEEK_IMP (m_imp, T, t)
class UVMBlockingPeekImp():
    pass
UVMBlockingPeekImp = UVM_IMP_COMMON(UVMBlockingPeekImp, UVM_TLM_BLOCKING_PEEK_MASK,"uvm_blocking_peek_imp")
UVM_BLOCKING_PEEK_IMP('m_imp', UVMBlockingPeekImp)

#class uvm_nonblocking_peek_imp #(type T=int, type IMP=int)
#  extends uvm_port_base #(uvm_tlm_if_base #(T,T));
#  `UVM_IMP_COMMON(`UVM_TLM_NONBLOCKING_PEEK_MASK,"uvm_nonblocking_peek_imp",IMP)
#  `UVM_NONBLOCKING_PEEK_IMP (m_imp, T, t)
class UVMNonBlockingPeekImp():
    pass
UVMNonBlockingPeekImp = UVM_IMP_COMMON(UVMNonBlockingPeekImp, UVM_TLM_NONBLOCKING_PEEK_MASK, "uvm_nonblocking_peek_imp")
UVM_NONBLOCKING_PEEK_IMP('m_imp', UVMNonBlockingPeekImp)

#class uvm_peek_imp #(type T=int, type IMP=int)
#  extends uvm_port_base #(uvm_tlm_if_base #(T,T));
#  `UVM_IMP_COMMON(`UVM_TLM_PEEK_MASK,"uvm_peek_imp",IMP)
#  `UVM_PEEK_IMP (m_imp, T, t)
#endclass
class UVMPeekImp():
    pass
UVMPeekImp = UVM_IMP_COMMON(UVMPeekImp, UVM_TLM_PEEK_MASK,"uvm_peek_imp")
UVM_PEEK_IMP ('m_imp', UVMPeekImp)

#class uvm_blocking_get_peek_imp #(type T=int, type IMP=int)
#  extends uvm_port_base #(uvm_tlm_if_base #(T,T));
#  `UVM_IMP_COMMON(`UVM_TLM_BLOCKING_GET_PEEK_MASK,"uvm_blocking_get_peek_imp",IMP)
#  `UVM_BLOCKING_GET_PEEK_IMP (m_imp, T, t)
class UVMBlockingGetPeekImp():
    pass
UVMBlockingGetPeekImp = UVM_IMP_COMMON(UVMBlockingGetPeekImp, UVM_TLM_BLOCKING_GET_PEEK_MASK, "uvm_blocking_get_peek_imp")
UVM_BLOCKING_GET_PEEK_IMP ('m_imp', UVMBlockingGetPeekImp)

#class uvm_nonblocking_get_peek_imp #(type T=int, type IMP=int)
#  extends uvm_port_base #(uvm_tlm_if_base #(T,T));
#  `UVM_IMP_COMMON(`UVM_TLM_NONBLOCKING_GET_PEEK_MASK,"uvm_nonblocking_get_peek_imp",IMP)
#  `UVM_NONBLOCKING_GET_PEEK_IMP (m_imp, T, t)
class UVMNonBlockingGetPeekImp():
    pass
UVMNonBlockingGetPeekImp = UVM_IMP_COMMON(UVMNonBlockingGetPeekImp,UVM_TLM_NONBLOCKING_GET_PEEK_MASK,"uvm_nonblocking_get_peek_imp")
UVM_NONBLOCKING_GET_PEEK_IMP ('m_imp', UVMNonBlockingGetPeekImp)

#class uvm_get_peek_imp #(type T=int, type IMP=int)
#  extends uvm_port_base #(uvm_tlm_if_base #(T,T));
#  `UVM_IMP_COMMON(`UVM_TLM_GET_PEEK_MASK,"uvm_get_peek_imp",IMP)
#  `UVM_GET_PEEK_IMP (m_imp, T, t)
class UVMGetPeekImp():
    pass
UVMGetPeekImp = UVM_IMP_COMMON(UVMGetPeekImp, UVM_TLM_GET_PEEK_MASK,"uvm_get_peek_imp")
UVM_GET_PEEK_IMP('m_imp', UVMGetPeekImp)

#//------------------------------------------------------------------------------
#//
#// CLASS: uvm_*_imp #(REQ, RSP, IMP, REQ_IMP, RSP_IMP)
#//
#// Bidirectional implementation (imp) port classes--An imp port provides access
#// to an implementation of the associated interface to all connected ~ports~ and
#// ~exports~. Each imp port instance ~must~ be connected to the component instance
#// that implements the associated interface, typically the imp port's parent.
#// All other connections-- e.g. to other ports and exports-- are prohibited.
#//
#// The interface represented by the asterisk is any of the following
#//
#//|  blocking_transport
#//|  nonblocking_transport
#//|  transport
#//|
#//|  blocking_master
#//|  nonblocking_master
#//|  master
#//|
#//|  blocking_slave
#//|  nonblocking_slave
#//|  slave
#//
#// Type parameters
#//
#// REQ  - Request transaction type
#//
#// RSP  - Response transaction type
#//
#// IMP  - Component type that implements the interface methods, typically the
#//        the parent of this imp port.
#//
#// REQ_IMP - Component type that implements the request side of the
#//           interface. Defaults to IMP. For master and slave imps only.
#//
#// RSP_IMP - Component type that implements the response side of the
#//           interface. Defaults to IMP. For master and slave imps only.
#//
#// The interface methods are implemented in a component of type ~IMP~, a handle
#// to which is passed in a constructor argument.  The imp port delegates all
#// interface calls to this component.
#//
#// The master and slave imps have two modes of operation.
#//
#// - A single component of type IMP implements the entire interface for
#//   both requests and responses.
#//
#// - Two sibling components of type REQ_IMP and RSP_IMP implement the request
#//   and response interfaces, respectively.  In this case, the IMP parent
#//   instantiates this imp port ~and~ the REQ_IMP and RSP_IMP components.
#//
#// The second mode is needed when a component instantiates more than one imp
#// port, as in the <uvm_tlm_req_rsp_channel #(REQ,RSP)> channel.
#//
#//------------------------------------------------------------------------------


#// Function: new
#//
#// Creates a new bidirectional imp port with the given ~name~ and ~parent~.
#// The ~parent~, whose type is specified by ~IMP~ type parameter,
#// must implement the interface associated with this port.
#//
#// Transport imp constructor
#//
#//|  function new(string name, IMP imp)
#//
#// Master and slave imp constructor
#//
#// The optional ~req_imp~ and ~rsp_imp~ arguments, available to master and
#// slave imp ports, allow the requests and responses to be handled by different
#// subcomponents. If they are specified, they must point to the underlying
#// component that implements the request and response methods, respectively.
#//
#//|  function new(string name, IMP imp,
#//|                            REQ_IMP req_imp=imp, RSP_IMP rsp_imp=imp)
#

#class uvm_blocking_master_imp #(type REQ=int, type RSP=REQ, type IMP=int,
#                                type REQ_IMP=IMP, type RSP_IMP=IMP)
#  extends uvm_port_base #(uvm_tlm_if_base #(REQ, RSP));
#  typedef IMP     this_imp_type;
#  typedef REQ_IMP this_req_type;
#  typedef RSP_IMP this_rsp_type;
#  `UVM_MS_IMP_COMMON(`UVM_TLM_BLOCKING_MASTER_MASK,"uvm_blocking_master_imp")
#  `UVM_BLOCKING_PUT_IMP (m_req_imp, REQ, t)
#  `UVM_BLOCKING_GET_PEEK_IMP (m_rsp_imp, RSP, t)
#endclass
class UVMBlockingMasterImp():  #(type REQ=int, type RSP=REQ, type IMP=int,
    pass
UVMBlockingMasterImp =  UVM_MS_IMP_COMMON(UVMBlockingMasterImp, UVM_TLM_BLOCKING_MASTER_MASK,"uvm_blocking_master_imp")
UVM_BLOCKING_PUT_IMP('m_req_imp', UVMBlockingMasterImp)
UVM_BLOCKING_GET_PEEK_IMP('m_rsp_imp', UVMBlockingMasterImp)


#class uvm_nonblocking_master_imp #(type REQ=int, type RSP=REQ, type IMP=int,
#                                   type REQ_IMP=IMP, type RSP_IMP=IMP)
#  extends uvm_port_base #(uvm_tlm_if_base #(REQ, RSP));
#  typedef IMP     this_imp_type;
#  typedef REQ_IMP this_req_type;
#  typedef RSP_IMP this_rsp_type;
#  `UVM_MS_IMP_COMMON(`UVM_TLM_NONBLOCKING_MASTER_MASK,"uvm_nonblocking_master_imp")
#  `UVM_NONBLOCKING_PUT_IMP (m_req_imp, REQ, t)
#  `UVM_NONBLOCKING_GET_PEEK_IMP (m_rsp_imp, RSP, t)
#endclass
class UVMNonBlockingMasterImp():  # (type REQ=int, type RSP=REQ, type IMP=int,
    pass
UVMNonBlockingMasterImp =  UVM_MS_IMP_COMMON(UVMNonBlockingMasterImp, UVM_TLM_NONBLOCKING_MASTER_MASK,"uvm_nonblocking_master_imp")
UVM_NONBLOCKING_PUT_IMP ('m_req_imp', UVMNonBlockingMasterImp)
UVM_NONBLOCKING_GET_PEEK_IMP ('m_rsp_imp', UVMNonBlockingMasterImp)


#class uvm_master_imp #(type REQ=int, type RSP=REQ, type IMP=int,
#                       type REQ_IMP=IMP, type RSP_IMP=IMP)
#  extends uvm_port_base #(uvm_tlm_if_base #(REQ, RSP));
#  typedef IMP     this_imp_type;
#  typedef REQ_IMP this_req_type;
#  typedef RSP_IMP this_rsp_type;
#  `UVM_MS_IMP_COMMON(`UVM_TLM_MASTER_MASK,"uvm_master_imp")
#  `UVM_PUT_IMP (m_req_imp, REQ, t)
#  `UVM_GET_PEEK_IMP (m_rsp_imp, RSP, t)
#endclass
class UVMMasterImp:
    pass
UVMMasterImp = UVM_MS_IMP_COMMON(UVMMasterImp, UVM_TLM_MASTER_MASK, "uvm_master_imp")
UVM_PUT_IMP('m_req_imp', UVMMasterImp)
UVM_GET_PEEK_IMP('m_rsp_imp', UVMMasterImp)


#class uvm_blocking_slave_imp #(type REQ=int, type RSP=REQ, type IMP=int,
#                               type REQ_IMP=IMP, type RSP_IMP=IMP)
#  extends uvm_port_base #(uvm_tlm_if_base #(RSP, REQ));
#  typedef IMP     this_imp_type;
#  typedef REQ_IMP this_req_type;
#  typedef RSP_IMP this_rsp_type;
#  `UVM_MS_IMP_COMMON(`UVM_TLM_BLOCKING_SLAVE_MASK,"uvm_blocking_slave_imp")
#  `UVM_BLOCKING_PUT_IMP (m_rsp_imp, RSP, t)
#  `UVM_BLOCKING_GET_PEEK_IMP (m_req_imp, REQ, t)
#endclass
class UVMBlockingSlaveImp():
    pass
UVMBlockingSlaveImp = UVM_MS_IMP_COMMON(UVMBlockingSlaveImp, 
    UVM_TLM_BLOCKING_SLAVE_MASK,"uvm_blocking_slave_imp")
UVM_BLOCKING_PUT_IMP('m_rsp_imp', UVMBlockingSlaveImp)
UVM_BLOCKING_GET_PEEK_IMP ('m_req_imp', UVMBlockingSlaveImp)

#class uvm_nonblocking_slave_imp #(type REQ=int, type RSP=REQ, type IMP=int,
#                                  type REQ_IMP=IMP, type RSP_IMP=IMP)
#  extends uvm_port_base #(uvm_tlm_if_base #(RSP, REQ));
#  typedef IMP     this_imp_type;
#  typedef REQ_IMP this_req_type;
#  typedef RSP_IMP this_rsp_type;
#  `UVM_MS_IMP_COMMON(`UVM_TLM_NONBLOCKING_SLAVE_MASK,"uvm_nonblocking_slave_imp")
#  `UVM_NONBLOCKING_PUT_IMP (m_rsp_imp, RSP, t)
#  `UVM_NONBLOCKING_GET_PEEK_IMP (m_req_imp, REQ, t)
#endclass
class UVMNonBlockingSlaveImp():   # (type REQ=int, type RSP=REQ, type IMP=int,
    pass
UVMNonBlockingSlaveImp = UVM_MS_IMP_COMMON(UVMNonBlockingSlaveImp,
    UVM_TLM_NONBLOCKING_SLAVE_MASK,"uvm_nonblocking_slave_imp")
UVM_NONBLOCKING_PUT_IMP('m_rsp_imp', UVMNonBlockingSlaveImp)
UVM_NONBLOCKING_GET_PEEK_IMP('m_req_imp', UVMNonBlockingSlaveImp)

#class uvm_slave_imp #(type REQ=int, type RSP=REQ, type IMP=int,
#                      type REQ_IMP=IMP, type RSP_IMP=IMP)
#  extends uvm_port_base #(uvm_tlm_if_base #(RSP, REQ));
#  typedef IMP     this_imp_type;
#  typedef REQ_IMP this_req_type;
#  typedef RSP_IMP this_rsp_type;
#  `UVM_MS_IMP_COMMON(`UVM_TLM_SLAVE_MASK,"uvm_slave_imp")
#  `UVM_PUT_IMP (m_rsp_imp, RSP, t)
#  `UVM_GET_PEEK_IMP (m_req_imp, REQ, t)
#endclass
class UVMSlaveImp:
    pass
UVMSlaveImp = UVM_MS_IMP_COMMON(UVMSlaveImp, UVM_TLM_SLAVE_MASK, "uvm_slave_imp")
UVM_PUT_IMP ('m_rsp_imp', UVMSlaveImp)
UVM_GET_PEEK_IMP('m_req_imp', UVMSlaveImp)


#class uvm_blocking_transport_imp #(type REQ=int, type RSP=REQ, type IMP=int)
#  extends uvm_port_base #(uvm_tlm_if_base #(REQ, RSP));
#  `UVM_IMP_COMMON(`UVM_TLM_BLOCKING_TRANSPORT_MASK,"uvm_blocking_transport_imp",IMP)
#  `UVM_BLOCKING_TRANSPORT_IMP (m_imp, REQ, RSP, req, rsp)
#endclass
class UVMBlockingTransportImp():  # (type REQ=int, type RSP=REQ, type IMP=int)
    pass
UVMBlockingTransportImp = UVM_IMP_COMMON(UVMBlockingTransportImp,
    UVM_TLM_BLOCKING_TRANSPORT_MASK,"uvm_blocking_transport_imp")
UVM_BLOCKING_TRANSPORT_IMP('m_imp', UVMBlockingTransportImp)

#class uvm_nonblocking_transport_imp #(type REQ=int, type RSP=REQ, type IMP=int)
#  extends uvm_port_base #(uvm_tlm_if_base #(REQ, RSP));
#  `UVM_IMP_COMMON(`UVM_TLM_NONBLOCKING_TRANSPORT_MASK,"uvm_nonblocking_transport_imp",IMP)
#  `UVM_NONBLOCKING_TRANSPORT_IMP (m_imp, REQ, RSP, req, rsp)
#endclass
class UVMNonBlockingTransportImp():  # (type REQ=int, type RSP=REQ, type IMP=int)
    pass
UVMNonBlockingTransportImp = UVM_IMP_COMMON(UVMNonBlockingTransportImp,
    UVM_TLM_NONBLOCKING_TRANSPORT_MASK,"uvm_nonblocking_transport_imp")
UVM_NONBLOCKING_TRANSPORT_IMP ('m_imp', UVMNonBlockingTransportImp)

#class uvm_transport_imp #(type REQ=int, type RSP=REQ, type IMP=int)
#  extends uvm_port_base #(uvm_tlm_if_base #(REQ, RSP));
#  `UVM_IMP_COMMON(`UVM_TLM_TRANSPORT_MASK,"uvm_transport_imp",IMP)
#  `UVM_BLOCKING_TRANSPORT_IMP (m_imp, REQ, RSP, req, rsp)
#  `UVM_NONBLOCKING_TRANSPORT_IMP (m_imp, REQ, RSP, req, rsp)
#endclass
class UVMTransportImp:
    pass
UVMTransportImp = UVM_IMP_COMMON(UVMTransportImp, UVM_TLM_TRANSPORT_MASK, "uvm_transport_imp")
UVM_BLOCKING_TRANSPORT_IMP('m_imp', UVMTransportImp)
UVM_NONBLOCKING_TRANSPORT_IMP('m_imp', UVMTransportImp)
