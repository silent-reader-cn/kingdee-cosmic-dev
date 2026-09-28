# 付款预警设置-cas_paywarnset

## 付款预警设置-主表 t_cas_paywarnset

- **表名称：** 付款预警设置-主表
- **表名：** t_cas_paywarnset

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fissubmit | 提交 | bpchar | 1 |  | √ | '0' | 提交 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fissameusage | 转账附言相同 | bpchar | 1 |  | √ | '0' | 转账附言相同 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fissamepayee | 收款人相同 | bpchar | 1 |  | √ | '0' | 收款人相同 |
| 7 | fissamepayamt | 付款金额相同 | bpchar | 1 |  | √ | '0' | 付款金额相同 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fcheckdays | 校验周期（天） | int8 | 64 |  | √ | 0 | 校验周期（天） |
| 11 | fissamesettletype | 结算方式相同 | bpchar | 1 |  | √ | '0' | 结算方式相同 |
| 12 | fenable | 状态 | bpchar | 1 |  | √ | '0' | 状态,枚举: 0 :禁用 1 :启用 |
| 13 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 14 | fissamepayerbanknum | 付款账号相同 | bpchar | 1 |  | √ | '0' | 付款账号相同 |
| 15 | fbilltype | 单据类型 | varchar | 30 |  | √ | ' ' | 单据类型,枚举: cas_paybill :付款单 cas_agentpaybill :代发单 |
| 16 | fiscombei | 提交银企 | bpchar | 1 |  | √ | '0' | 提交银企 |
| 17 | fissamepayeebanknum | 收款账号相同 | bpchar | 1 |  | √ | '0' | 收款账号相同 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pws_fbilltype |  | fbilltype |
| 2 | t_cas_paywarnset_pkey |  | fid |

---

## 单据体-子表 t_cas_paywarnentry

- **表名称：** 单据体-子表
- **表名：** t_cas_paywarnentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | forgid | 组织编码 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cas_pwe_id |  | fid |
| 2 | t_cas_paywarnentry_pkey |  | fentryid |
