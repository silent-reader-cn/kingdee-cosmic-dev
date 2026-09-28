# 外部企业黑名单表-rim_black_list_data

## 外部企业黑名单表-主表 t_rim_black_list_data2

- **表名称：** 外部企业黑名单表-主表
- **表名：** t_rim_black_list_data2

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcase_type | 案件类型 | varchar | 50 |  | √ | ' ' | 案件类型 |
| 3 | fcase_detail | 案件明细 | varchar | 600 |  | √ | ' ' | 案件明细 |
| 4 | flegal_card_no | 法定代表人证件号 | varchar | 100 |  | √ | ' ' | 法定代表人证件号 |
| 5 | fpublic_date | 公示日期 | timestamp | 0 |  |  | null | 公示日期 |
| 6 | fcase_nature | 案件性质 | varchar | 100 |  | √ | ' ' | 案件性质 |
| 7 | flegal_card_type | 法定代表人证件类型 | varchar | 50 |  | √ | ' ' | 法定代表人证件类型 |
| 8 | flegal_sex | 法定代表人性别 | varchar | 100 |  | √ | ' ' | 法定代表人性别 |
| 9 | ftax_payer_no | 纳税人识别号 | varchar | 50 |  | √ | ' ' | 纳税人识别号 |
| 10 | fexecute_result | 处罚结果 | varchar | 200 |  | √ | ' ' | 处罚结果 |
| 11 | fupdate_date | 更新日期 | timestamp | 0 |  |  | null | 更新日期 |
| 12 | forg | 组织机构代码 | varchar | 100 |  | √ | ' ' | 组织机构代码 |
| 13 | fmedium_info | 直接责任中介 | varchar | 200 |  | √ | ' ' | 直接责任中介 |
| 14 | fexecute_no | 处罚文书号 | varchar | 50 |  | √ | ' ' | 处罚文书号 |
| 15 | fexecute_department | 行政机关 | varchar | 150 |  | √ | ' ' | 行政机关 |
| 16 | fregister_date | 登记日期 | timestamp | 0 |  |  | null | 登记日期 |
| 17 | fcount | 处罚次数 | int8 | 64 |  | √ | 0 | 处罚次数 |
| 18 | fcompany_name | 企业名称 | varchar | 200 |  | √ | ' ' | 企业名称 |
| 19 | fblack_list_type | 黑名单类型 | varchar | 50 |  | √ | ' ' | 黑名单类型,枚举: 1 :税收黑名单 2 :经营违法 3 :税收违法 4 :白名单 |
| 20 | flegal_name | 法定代表人姓名 | varchar | 80 |  | √ | ' ' | 法定代表人姓名 |
| 21 | fprovince | 省份 | varchar | 50 |  | √ | ' ' | 省份 |
| 22 | fregist_address | 注册地址 | varchar | 300 |  | √ | ' ' | 注册地址 |
| 23 | fcreate_date | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rim_black_list_data2 |  | ftax_payer_no |
| 2 | pk_rim_black_list_data2 |  | fid |
