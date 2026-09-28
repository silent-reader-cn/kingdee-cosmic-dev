# 进项转出分摊明细单据-tcvat_apportion_detail

## 进项转出分摊明细单据-主表 t_tcvat_apportion_detail

- **表名称：** 进项转出分摊明细单据-主表
- **表名：** t_tcvat_apportion_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcurrentregistertaxamount | 本次登记税额 | numeric | 23 | 10 | √ | 0.0000000000 | 本次登记税额 |
| 3 | fregistercoshareid | 登记关联分摊id | varchar | 50 |  | √ | ' ' | 登记关联分摊id |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | frollouttype | 进项转出类型 | varchar | 30 |  | √ | ' ' | 进项转出类型,枚举: 1 :免税项目用 2 :集体福利、个人消费 3 :非正常损失 4 :简易计税项目用 5 :开具红字专用发票信息表 6 :其他 7 :免税项目用、简易计税项目用 |
| 7 | fincomesummary | 收入总额 | numeric | 23 | 10 | √ | 0.0000000000 | 收入总额 |
| 8 | fapportionrate | 划分比例 | numeric | 23 | 10 | √ | 0.0000000000 | 划分比例 |
| 9 | fapportiontype | 分摊类型 | varchar | 30 |  | √ | ' ' | 分摊类型,枚举: 1 :分摊计算 2 :取消分摊 |
| 10 | fapportioncreatetime | 分摊创建日期 | timestamp | 0 |  |  | null | 分摊创建日期 |
| 11 | fapportiontaxamount | 分摊税额 | numeric | 23 | 10 | √ | 0.0000000000 | 分摊税额 |
| 12 | fconsumertype | 进项转出用途标识 | varchar | 30 |  | √ | ' ' | 进项转出用途标识,枚举: 1 :免税项目用 2 :集体福利、个人消费 3 :非正常损失 4 :简易计税项目用 5 :开具红字专用发票信息表 6 :其他 7 :无法划分 : |
| 13 | fprojectincome | 项目收入 | numeric | 23 | 10 | √ | 0.0000000000 | 项目收入 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | frollouttaxperiod | 转出所属税期 | varchar | 50 |  | √ | ' ' | 转出所属税期 |
| 16 | fapportionstatus | 分摊状态 | varchar | 30 |  | √ | ' ' | 分摊状态,枚举: 1 :已分摊 2 :未分摊 |
| 17 | fapportionmodifytime | 分摊修改日期 | timestamp | 0 |  |  | null | 分摊修改日期 |
| 18 | fsummaryflag | 标志位 | varchar | 30 |  | √ | ' ' | 标志位,枚举: 0 :标志位0 1 :标志位1 |
| 19 | fapportionremark | 分摊备注 | varchar | 125 |  | √ | ' ' | 分摊备注 |
| 20 | fshareid | 外键id | varchar | 50 |  | √ | ' ' | 外键id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcvat_apportion_detail |  | forgid,frollouttaxperiod |
| 2 | t_tcvat_apportion_detail_pkey |  | fid |
