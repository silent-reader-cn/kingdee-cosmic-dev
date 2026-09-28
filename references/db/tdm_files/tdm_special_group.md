# 特殊群体信息-tdm_special_group

## 特殊群体信息-主表 t_tdm_special_group

- **表名称：** 特殊群体信息-主表
- **表名：** t_tdm_special_group

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fjoindate | 入职日期 | timestamp | 0 |  |  | null | 入职日期 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fstaffname | 员工姓名 | varchar | 255 |  | √ | ' ' | 员工姓名 |
| 5 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fstaffnumber | 员工号 | varchar | 36 |  | √ | ' ' | 员工号 |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fdatefield1 | 证件失效日期 | timestamp | 0 |  |  | null | 证件失效日期 |
| 10 | fidnumber | 身份证号码 | varchar | 20 |  | √ | ' ' | 身份证号码 |
| 11 | fdatefield | 证件生效日期 | timestamp | 0 |  |  | null | 证件生效日期 |
| 12 | forg | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fleavedate | 离职日期 | timestamp | 0 |  |  | null | 离职日期 |
| 15 | fcertcode | 证件编号 | varchar | 50 |  | √ | ' ' | 证件编号 |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | ftype | 特殊群体类型 | varchar | 50 |  | √ | ' ' | 特殊群体类型,枚举: 0 :残疾人 1 :自主就业退役士兵 2 :建档立卡贫困人口 3 :登记失业半年以上人员 4 :毕业年度内高校毕业生 |
| 18 | fssstartmonth | 缴纳社保起始月份 | timestamp | 0 |  |  | null | 缴纳社保起始月份 |
| 19 | fbillno | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 20 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 21 | fpayssonresignmonth | 离职当月是否缴纳社保 | varchar | 50 |  | √ | ' ' | 离职当月是否缴纳社保,枚举: 1 :是 0 :否 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tdm_special_org |  | forg |
| 2 | pk_tdm_special_group |  | fid |
