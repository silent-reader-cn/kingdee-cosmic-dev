# 交单计划数据存储-mrp_rpt_decuments_datas

## 交单计划数据存储-主表 t_mrp_decuments_datas

- **表名称：** 交单计划数据存储-主表
- **表名：** t_mrp_decuments_datas

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
| 1 | pk_t_mrp_decuments_datas |  | fid |
| 2 | idx_mrp_decuments_datas |  | fbillno |

---

## 单据体-子表 t_mrp_decuments_datafix

- **表名称：** 单据体-子表
- **表名：** t_mrp_decuments_datafix

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | freleasetime | 发布时间 | timestamp | 0 |  |  | null | 发布时间 |
| 3 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 4 | fsupplyorg | 供应组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | freleaseuser | 发布人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | foperator | 产品计划员 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | ftotalqty | 合计 | numeric | 23 | 10 | √ | 0 | 合计 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | freleasestatus | 发布状态 | varchar | 50 |  | √ | ' ' | 发布状态,枚举: A :未发布 B :已发布 |
| 10 | fnonstandardqty | 非标数量 | numeric | 23 | 10 | √ | 0 | 非标数量 |
| 11 | fentry_modifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fdemandmodel | 计划模式 | varchar | 50 |  | √ | ' ' | 计划模式,枚举: MTS :MTS MTO :MTO ATO :ATO ETO :ETO STO :STO |
| 13 | fgoodprodinvqty | 良品库存 | numeric | 23 | 10 | √ | 0 | 良品库存 |
| 14 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fiscommitment | 是否承诺 | varchar | 50 |  | √ | ' ' | 是否承诺,枚举: A :未承诺 B :已承诺 |
| 16 | fmodifydatefield | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 17 | fmaterial | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 18 | fdefprodinvqty | 三品数量 | numeric | 23 | 10 | √ | 0 | 三品数量 |
| 19 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 20 | fmodelnum | 规格型号 | varchar | 255 |  | √ | ' ' | 规格型号 |
| 21 | fmaterialname | 物料名称 | varchar | 255 |  | √ | ' ' | 物料名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mrp_decuments_datafix |  | fid,fseq |
| 2 | pk_t_mrp_decuments_datafix |  | fentryid |

---

## 子单据体-子表 t_mrp_decuments_datasub

- **表名称：** 子单据体-子表
- **表名：** t_mrp_decuments_datasub

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
| 1 | pk_t_mrp_decuments_datasub |  | fdetailid |
| 2 | idx_mrp_decuments_datasub |  | fentryid,fseq |
