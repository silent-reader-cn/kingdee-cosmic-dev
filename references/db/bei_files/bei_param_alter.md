# 敏感参数变更单-bei_param_alter

## 签署人单据体-子表 t_bei_alterconfirmentity

- **表名称：** 签署人单据体-子表
- **表名：** t_bei_alterconfirmentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdisclaimercontent | 风险告知内容 | varchar | 255 |  | √ | ' ' | 风险告知内容 |
| 3 | fdisclaimername | 风险告知 | varchar | 255 |  | √ | ' ' | 风险告知 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fdisclaimercontent_tag | 风险告知内容_详情 | text | 0 |  |  | null | 风险告知内容_详情 |
| 6 | fconfirmtime | 签署时间 | timestamp | 0 |  |  | null | 签署时间 |
| 7 | fconfirmuser | 签署人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fconfirmusetype | 签署人类型 | varchar | 30 |  | √ | ' ' | 签署人类型,枚举: A :签署人 B :知悉人 |
| 10 | fdisclaimerid | fdisclaimerid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bei_alterconfirmentity |  | fentryid |

---

## 敏感参数变更单-主表 t_bei_paramalter

- **表名称：** 敏感参数变更单-主表
- **表名：** t_bei_paramalter

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fintervaloldparam | 付款状态变更为交易失败时间间隔 | varchar | 30 |  | √ | ' ' | 付款状态变更为交易失败时间间隔,枚举: 0 :提交银企12个小时后 1 :提交银企4个小时后 2 :提交银企1个小时后 |
| 4 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 变更申请组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fapplyuser | 变更申请人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | freason | 变更申请原因 | varchar | 255 |  | √ | ' ' | 变更申请原因 |
| 10 | fintervalnewparam | 付款状态变更为交易失败时间间隔 | varchar | 30 |  | √ | ' ' | 付款状态变更为交易失败时间间隔,枚举: 0 :提交银企12个小时后 1 :提交银企4个小时后 2 :提交银企1个小时后 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | faltertype | 变更参数 | varchar | 30 |  | √ | ' ' | 变更参数,枚举: bei003 :付款状态变更为交易失败时间 |
| 14 | fbizdate | 变更申请时间 | timestamp | 0 |  |  | null | 变更申请时间 |
| 15 | fbillno | 单据编号 | varchar | 100 |  | √ | ' ' | 单据编号 |
| 16 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bei_paramalter |  | fid |
