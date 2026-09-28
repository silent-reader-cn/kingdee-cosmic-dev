# 取数项目映射-ipo_item_mapping_bill

## 取数项目映射-主表 t_theme_item_mapping

- **表名称：** 取数项目映射-主表
- **表名：** t_theme_item_mapping

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | faccounttype | 科目类型 | varchar | 50 |  | √ | ' ' | 科目类型,枚举: 0 :合并报表 1 :报表 |
| 6 | frptitemid | 报表项目 | int8 | 64 |  | √ | 0 | 报表项目 xkbd_rptitem |
| 7 | fbusinessitem | 企业版项目 | int8 | 64 |  | √ | 0 | 企业版项目 ipo_business_item |
| 8 | ffinreportitemld | IPO财务报表项目 | int8 | 64 |  | √ | 0 | 财务报表项目 ipo_fin_report_item |
| 9 | fipoorgld | IPO主体 | int8 | 64 |  | √ | 0 | IPO编制组织 ipo_org |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_theme_item_mapping |  | fid |
| 2 | item_mapping_index |  | fipoorgld |
