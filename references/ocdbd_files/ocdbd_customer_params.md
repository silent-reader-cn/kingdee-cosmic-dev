# 企业组织参数-ocdbd_customer_params

## 时间分录-子表 t_ocdbd_param_timeentity

- **表名称：** 时间分录-子表
- **表名：** t_ocdbd_param_timeentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fbegintimemillis | 开始时间 | int4 | 32 |  | √ | 0 | 开始时间 |
| 4 | fendtime | 结束时间_作废 | timestamp | 0 |  |  | null | 结束时间_作废 |
| 5 | fendtimemillis | 结束时间 | int4 | 32 |  | √ | 0 | 结束时间 |
| 6 | foperation | 操作 | varchar | 30 |  | √ | ' ' | 操作,枚举: save :保存 submit :提交 audit :审核 |
| 7 | fisuse | 启用 | bpchar | 1 |  | √ | '0' | 启用 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fstarttime | 开始时间_作废 | timestamp | 0 |  |  | null | 开始时间_作废 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_param_timeentity |  | fentryid |
| 2 | idx_ocdbd_paramtimeentity_fid |  | fid |

---

## 企业组织参数-主表 t_ocdbd_customer_params

- **表名称：** 企业组织参数-主表
- **表名：** t_ocdbd_customer_params

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fallotcontroltype | 可销量控制强度 | bpchar | 1 |  | √ | ' ' | 可销量控制强度,枚举: 0 :不控制 2 :警告 1 :强控制 |
| 3 | fstockoutshowtype | 时，库存模糊显示为 | bpchar | 1 |  | √ | '1' | 时，库存模糊显示为,枚举: 1 :固定文字 2 :精确数字 |
| 4 | fenddatetime | 下单结束时间 | timestamp | 0 |  |  | null | 下单结束时间 |
| 5 | fenabletension |  | bpchar | 1 |  | √ | '1' |  |
| 6 | fiskneadprice | 要货订单到销售订单揉价处理 | bpchar | 1 |  | √ | '0' | 要货订单到销售订单揉价处理 |
| 7 | fstockoutqty | 当可用库存量 <= | int4 | 32 |  | √ | 0 | 当可用库存量 <= |
| 8 | fissignuploadimg | 签收必须上传图片 | bpchar | 1 |  | √ | '0' | 签收必须上传图片 |
| 9 | fcppallowzerocontrol | 渠道价格政策单价和折扣非空控制 | bpchar | 1 |  | √ | '1' | 渠道价格政策单价和折扣非空控制,枚举: 0 :不控制 2 :警告 1 :强控制 |
| 10 | fisbyocbmall | 经销商门户（PC+移动）端控制 | bpchar | 1 |  | √ | '0' | 经销商门户（PC+移动）端控制 |
| 11 | fisallot | 启用可销量控制 | bpchar | 1 |  | √ | '0' | 启用可销量控制 |
| 12 | fsignovertime | 超时时间（小时） | int4 | 32 |  | √ | 24 | 超时时间（小时） |
| 13 | fenableenough |  | bpchar | 1 |  | √ | '1' |  |
| 14 | ftensionbeginqty | 当可用库存量 > | int4 | 32 |  | √ | 0 | 当可用库存量 > |
| 15 | fenoughshowvalue |  | varchar | 50 |  | √ | ' ' |  |
| 16 | finventorymatchtype | 即时库存控制强度 | bpchar | 1 |  | √ | 'A' | 即时库存控制强度,枚举: A :不控制 B :警告 C :强控制 |
| 17 | fsubsaleoverscope | 负卖到货冲减范围 | varchar | 50 |  | √ | ' ' | 负卖到货冲减范围,枚举: A :采购入库单 B :其他入库单 C :调拨入库单 D :生产入库单 E :销售退货单 |
| 18 | fisactivesign | 启用电子签章 | bpchar | 1 |  | √ | '0' | 启用电子签章 |
| 19 | ftensionendqty | ，<= | int4 | 32 |  | √ | 100 | ，<= |
| 20 | fsaleorgid | 销售组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 21 | fisbyocbsoc | 订单中心后台控制 | bpchar | 1 |  | √ | '0' | 订单中心后台控制 |
| 22 | ftensionshowtype | 时，库存模糊显示为 | bpchar | 1 |  | √ | '1' | 时，库存模糊显示为,枚举: 1 :固定文字 2 :精确数字 |
| 23 | fisinventorymatch | 使用共享库存规则 | bpchar | 1 |  | √ | '0' | 使用共享库存规则 |
| 24 | fenoughshowtype | 时，库存模糊显示为 | bpchar | 1 |  | √ | '1' | 时，库存模糊显示为,枚举: 1 :固定文字 2 :精确数字 |
| 25 | frecusetype | 订单收款抵扣行抵扣方式 | bpchar | 1 |  | √ | '1' | 订单收款抵扣行抵扣方式,枚举: 0 :自动抵扣 1 :手工抵扣 |
| 26 | fstartdatetime | 下单开始时间 | timestamp | 0 |  |  | null | 下单开始时间 |
| 27 | ftensionshowvalue |  | varchar | 50 |  | √ | ' ' |  |
| 28 | fisautosign | 超时自动签收 | bpchar | 1 |  | √ | '0' | 超时自动签收 |
| 29 | fisinvreserve | 启用即时库存控制 | bpchar | 1 |  | √ | '0' | 启用即时库存控制 |
| 30 | fstockoutshowvalue |  | varchar | 50 |  | √ | ' ' |  |
| 31 | fenoughqty | 当可用库存量 > | int4 | 32 |  | √ | 100 | 当可用库存量 > |
| 32 | fenablestockout |  | bpchar | 1 |  | √ | '1' |  |
| 33 | fisupdatestore | fisupdatestore | bpchar | 1 |  | √ | '1' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_customer_params |  | fid |
| 2 | idx_ocdbd_customerparams_sal |  | fsaleorgid |
