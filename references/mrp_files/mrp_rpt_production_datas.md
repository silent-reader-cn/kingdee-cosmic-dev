# 生产预测数据存储-mrp_rpt_production_datas

## 生产预测数据存储-主表 t_mrp_production_datas

- **表名称：** 生产预测数据存储-主表
- **表名：** t_mrp_production_datas

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fplanid | 计划运算号 | varchar | 100 |  | √ | ' ' | 计划运算号 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 9 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mrp_production_datas |  | fid |
| 2 | idx_mrp_production_datas |  | fbillno |

---

## 子单据体-子表 t_mrp_production_datasub

- **表名称：** 子单据体-子表
- **表名：** t_mrp_production_datasub

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | ffieldvalue | 值 | numeric | 23 | 10 | √ | 0 | 值 |
| 2 | fsequence | 顺序 | varchar | 50 |  | √ | ' ' | 顺序,枚举: 0 :0 1 :1 2 :2 3 :3 |
| 3 | ffieldcaption | 列展示名 | varchar | 50 |  | √ | ' ' | 列展示名 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 7 | ffieldkey | 列标识 | varchar | 50 |  | √ | ' ' | 列标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mrp_production_datasub |  | fdetailid |
| 2 | idx_mrp_production_datasub |  | fentryid,fseq |

---

## 单据体-子表 t_mrp_production_datafix

- **表名称：** 单据体-子表
- **表名：** t_mrp_production_datafix

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 50 |  | √ | ' ' | 备注 |
| 3 | fqty | 三品数量 | numeric | 23 | 10 | √ | 0 | 三品数量 |
| 4 | fofferingno | offering编码 | varchar | 50 |  | √ | ' ' | offering编码 |
| 5 | fsupplyorg | 供应组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fmanufacture | 制造策略 | int8 | 64 |  | √ | 0 | 制造策略 mpdm_manustrategy |
| 7 | foperator | 生产计划员 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | facqtime | 释放时间 | timestamp | 0 |  |  | null | 释放时间 |
| 9 | facquser | 释放人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | facqstatus | 释放状态 | varchar | 50 |  | √ | ' ' | 释放状态,枚举: A :未释放 B :已释放 |
| 11 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 12 | fmodifier | fmodifier | int8 | 64 |  | √ | 0 |  |
| 13 | fdemandmodel | 计划模式 | varchar | 30 |  | √ | ' ' | 计划模式,枚举: MTS :MTS MTO :MTO ATO :ATO ETO :ETO STO :STO |
| 14 | fofferingid | offeringID | int8 | 64 |  | √ | 0 | offeringID |
| 15 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 17 | fmodifydatefield | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 18 | fofferingname | offering名称 | varchar | 250 |  | √ | ' ' | offering名称 |
| 19 | fisdemandmaterial | 是否需求物料 | bpchar | 1 |  | √ | '1' | 是否需求物料 |
| 20 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mrp_production_datafix |  | fentryid |
| 2 | idx_mrp_production_datafix |  | fid,fseq |
