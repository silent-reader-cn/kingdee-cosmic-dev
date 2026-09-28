# 备料预测数据存储-mrp_rpt_stock_datas

## 备料预测数据存储-主表 t_mrp_stock_datas

- **表名称：** 备料预测数据存储-主表
- **表名：** t_mrp_stock_datas

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fplanid | 计划运算号 | varchar | 100 |  | √ | ' ' | 计划运算号 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 9 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mrp_stock_datas |  | fbillno |
| 2 | pk_t_mrp_stock_datas |  | fid |

---

## 单据体-子表 t_mrp_stock_datafix

- **表名称：** 单据体-子表
- **表名：** t_mrp_stock_datafix

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | freleasetime | 发布时间 | timestamp | 0 |  |  | null | 发布时间 |
| 3 | fremark | 备注 | varchar | 50 |  | √ | ' ' | 备注 |
| 4 | fisserviceuse | 是否服务专用编码 | varchar | 50 |  | √ | ' ' | 是否服务专用编码,枚举: |
| 5 | fsupplyorg | 供应组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | foperator | 产品计划员 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fweekqty | 当周发货 | numeric | 23 | 10 | √ | 0 | 当周发货 |
| 8 | fthreeqty | 三品数量 | numeric | 23 | 10 | √ | 0 | 三品数量 |
| 9 | finvqty | 排产库存 | numeric | 23 | 10 | √ | 0 | 排产库存 |
| 10 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 11 | freleasestatus | 发布状态 | varchar | 50 |  | √ | ' ' | 发布状态,枚举: |
| 12 | fdemandmodel | 计划模式 | varchar | 50 |  | √ | ' ' | 计划模式,枚举: MTS :MTS MTO :MTO ATO :ATO ETO :ETO STO :STO |
| 13 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fdullqty | 呆滞数量 | numeric | 23 | 10 | √ | 0 | 呆滞数量 |
| 15 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 16 | fmodifydatefield | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 17 | freleaser | 发布人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fmaterial | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 19 | ffirstreleasetime | 首次发布时间 | timestamp | 0 |  |  | null | 首次发布时间 |
| 20 | fmonthqty | 当月能力 | numeric | 23 | 10 | √ | 0 | 当月能力 |
| 21 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 22 | ffirstreleaser | 首次发布人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mrp_stock_datafix |  | fid |
| 2 | pk_t_mrp_stock_datafix |  | fentryid |

---

## 子单据体-子表 t_mrp_stock_datasub

- **表名称：** 子单据体-子表
- **表名：** t_mrp_stock_datasub

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | ffieldvalue | 值 | numeric | 30 | 10 | √ | 0 | 值 |
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
| 1 | idx_mrp_stock_datasub |  | fentryid |
| 2 | pk_t_mrp_stock_datasub |  | fdetailid |
