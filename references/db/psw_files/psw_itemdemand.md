# 生产线物料需求-psw_itemdemand

## 生产线物料需求-主表 t_psw_itemdemand

- **表名称：** 生产线物料需求-主表
- **表名：** t_psw_itemdemand

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  |  | null | 人员 bos_user |
| 3 | fcreatorid | 创建人 | int8 | 64 |  |  | null | 人员 bos_user |
| 4 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 6 | forgid | 组织 | int8 | 64 |  |  | null | 业务单元 bos_org |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 9 | fauditorid | 审核人 | int8 | 64 |  |  | null | 人员 bos_user |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 修改时间 |
| 11 | fmainmaterielid | 物料 | int8 | 64 |  |  | null | 物料 bd_material |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_psw_itemdemand |  | fbillno,fid |
| 2 | pk_t_psw_itemdemand |  | fid |

---

## 需求明细-子表 t_psw_itemplandetail

- **表名称：** 需求明细-子表
- **表名：** t_psw_itemplandetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmodifydatefield | 修改时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 修改时间 |
| 3 | fsrcentryid | 分录行内码 | int8 | 64 |  |  | null | 分录行内码 |
| 4 | fdemandtype | 需求类型 | bpchar | 1 |  | √ | ' ' | 需求类型,枚举: 0 :标准销售订单 1 :委托代销订单 2 :标准销售计划协议 3 :委托代销计划协议 4 :生产线独立需求 5 :重复生产用料清单 |
| 5 | fsrcbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 6 | fsrcbillid | 单据内码 | int8 | 64 |  |  | null | 单据内码 |
| 7 | fplandate | 计划日期 | timestamp | 0 |  |  | null | 计划日期 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fmodifierfield | 修改人 | int8 | 64 |  |  | null | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_psw_itemplandetail |  | fentryid |
| 2 | idx_t_psw_itemplandetail |  | fid |
