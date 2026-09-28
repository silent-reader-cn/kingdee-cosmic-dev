# 纳税人信用等级-tsate_credit_level_list

## 纳税人信用等级-主表 t_tsate_credit_level

- **表名称：** 纳税人信用等级-主表
- **表名：** t_tsate_credit_level

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fevaluationlevel | 评价等级 | varchar | 50 |  | √ | ' ' | 评价等级,枚举: A :A B :B C :C D :D M :M n : |
| 4 | fisstartcreditlevel | 是否发起信用等级 | varchar | 50 |  | √ | ' ' | 是否发起信用等级,枚举: 1 :是 0 :否 n : |
| 5 | fevaluationresult | 评价结果 | varchar | 50 |  | √ | ' ' | 评价结果,枚举: A :A B :B C :C D :D M :M zswwc :该纳税人终审未完成 |
| 6 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fupdatemsg | 更新操作提示 | varchar | 100 |  | √ | ' ' | 更新操作提示 |
| 9 | fbastaxtaxorg | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | fcomparemsg | 差异比对操作提示 | varchar | 100 |  | √ | ' ' | 差异比对操作提示 |
| 11 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fcreatedate | 下载时间 | timestamp | 0 |  |  | null | 下载时间 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fevaluationscore | 评价得分 | varchar | 50 |  | √ | ' ' | 评价得分 |
| 16 | fcomparestatus | 差异比对结果 | varchar | 50 |  | √ | 'undo' | 差异比对结果,枚举: comparing :比对中 diff :有差异 same :无差异 fail :比对失败 undo :未比对 |
| 17 | fisalldeal | 复核申请是否全部受理 | varchar | 50 |  | √ | ' ' | 复核申请是否全部受理,枚举: 1 :是 0 :否 n : |
| 18 | fupdatestatus | 更新状态 | varchar | 50 |  | √ | 'undo' | 更新状态,枚举: updating :更新中 updated :更新成功 fail :更新失败 without :无需更新 undo :未更新 |
| 19 | fevaluationyear | 评价年度 | varchar | 50 |  | √ | ' ' | 评价年度 |
| 20 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 21 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tsate_credit_level_org |  | fbastaxtaxorg,fevaluationyear |
| 2 | pk_tsate_credit_level |  | fid |
