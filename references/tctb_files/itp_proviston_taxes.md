# 税金计提单-itp_proviston_taxes

## 税金计提单-主表 t_itp_proviston_taxes

- **表名称：** 税金计提单-主表
- **表名：** t_itp_proviston_taxes

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | faccountorg | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | ftaxorg | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fprovistonitem | 计提事项 | int8 | 64 |  | √ | 0 | 计提事项 itp_proviston_item |
| 5 | fentitynumber | 来源底稿编号 | varchar | 200 |  | √ | ' ' | 来源底稿编号 |
| 6 | fentitytype | 来源底稿类型(要兼容) | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 7 | fvoucherno | 凭证号 | varchar | 50 |  | √ | ' ' | 凭证号 |
| 8 | ftaxarea | 税收辖区 | int8 | 64 |  | √ | 0 | 税收辖区 bastax_taxareagroup |
| 9 | fentrydate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fenddate | 计提期间.结束 | timestamp | 0 |  |  | null | 计提期间.结束 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | ftaxtype | 税种 | int8 | 64 |  | √ | 0 | 税种 bd_taxcategory |
| 14 | fsourcedrafttype | 来源底稿类型 | varchar | 100 |  | √ | ' ' | 来源底稿类型 |
| 15 | fbillno | 单据编号 | varchar | 200 |  | √ | ' ' | 单据编号 |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 18 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 19 | faccountsettype | 账簿类型 | varchar | 100 |  | √ | ' ' | 账簿类型 |
| 20 | fcoins | 计税币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 21 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 22 | ftaxsystem | 税收制度 | int8 | 64 |  | √ | 0 | 税收制度 bd_taxationsys |
| 23 | fstartdate | 计提期间.开始 | timestamp | 0 |  |  | null | 计提期间.开始 |
| 24 | fisvoucher | 生成凭证 | varchar | 50 |  | √ | ' ' | 生成凭证,枚举: 1 :是 0 :否 |
| 25 | ftotal | 税金合计 | numeric | 23 | 10 | √ | 0 | 税金合计 |
| 26 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_itp_proviston_taxes |  | fid |
| 2 | idx_proviston_taxes_no |  | fbillno |

---

## 单据体-子表 t_tctb_taxes_entry

- **表名称：** 单据体-子表
- **表名：** t_tctb_taxes_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbizdimensiontype | 业务维度 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 3 | ftaxitem | 税目 | varchar | 50 |  | √ | ' ' | 税目 |
| 4 | fbizdimensionname | 业务维度值 | varchar | 200 |  | √ | ' ' | 业务维度值 |
| 5 | fjtsj | 计提税金 | numeric | 23 | 10 | √ | 0 | 计提税金 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fbizdimensionid | 业务维度值ID | varchar | 50 |  | √ | ' ' | 业务维度值ID |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tctb_taxes_entry |  | fentryid |
| 2 | idx_tctb_taxes_entry_fk |  | fid |
