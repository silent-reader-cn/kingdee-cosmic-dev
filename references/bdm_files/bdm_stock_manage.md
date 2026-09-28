# 设备库存-bdm_stock_manage

## 单据体-子表 t_bdm_equip_stock_item

- **表名称：** 单据体-子表
- **表名：** t_bdm_equip_stock_item

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fuseorg | 使用组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bdm_equip_stock_item |  | fid |
| 2 | pk_t_bdm_equip_stock_item |  | fentryid |

---

## 设备库存-主表 t_bdm_equip_stock_manage

- **表名称：** 设备库存-主表
- **表名：** t_bdm_equip_stock_manage

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 用户1 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fequipmentno | 设备编号 | varchar | 50 |  | √ | ' ' | 设备编号 |
| 6 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 7 | feinvoicestock | 电票库存 | int8 | 64 |  | √ | 0 | 电票库存 |
| 8 | finvoicestock | 普票库存 | int8 | 64 |  | √ | 0 | 普票库存 |
| 9 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 10 | fepname | 企业名称 | varchar | 50 |  | √ | ' ' | 企业名称 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fequipmenttype | 设备类型 | varchar | 50 |  | √ | ' ' | 设备类型,枚举: 0 :税务Ukey 1 :税控盘 2 :金税盘 3 :虚拟Ukey 4 :托管 5 :区块链 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fespecialinvoicestock | 电专库存 | int8 | 64 |  | √ | 0 | 电专库存 |
| 15 | ftaxno | 纳税人识别号 | varchar | 50 |  | √ | ' ' | 纳税人识别号 |
| 16 | fspecialinvoicestock | 专票库存 | int8 | 64 |  | √ | 0 | 专票库存 |
| 17 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 18 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bdm_equip_stock_manage |  | fequipmentno |
| 2 | pk_bdm_equip_stock_manage |  | fid |
