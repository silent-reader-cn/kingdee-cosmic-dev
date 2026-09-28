# 对标报告记录-iba_report_record

## 对标报告记录-主表 t_iba_report_record

- **表名称：** 对标报告记录-主表
- **表名：** t_iba_report_record

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fjson | 报告参数 | varchar | 255 |  | √ | ' ' | 报告参数 |
| 3 | fdeletestate | 是否删除 | bpchar | 1 |  | √ | '0' | 是否删除 |
| 4 | flastdownloader | 最后下载人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | freportname | 报告名称 | varchar | 50 |  | √ | ' ' | 报告名称 |
| 6 | fdownloadnum | 已下载次数 | int8 | 64 |  | √ | 0 | 已下载次数 |
| 7 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 8 | flastdownloadtime | 最后下载时间 | timestamp | 0 |  |  | null | 最后下载时间 |
| 9 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fperiod | 报告期 | timestamp | 0 |  |  | null | 报告期 |
| 11 | fcurcompany | 本公司 | int8 | 64 |  | √ | 0 | IPO编制组织 ipo_org |
| 12 | fjson_tag | 报告参数_详情 | text | 0 |  |  | '' | 报告参数_详情 |
| 13 | fevaluatetype | 评价模型 | int8 | 64 |  | √ | 0 | 财务评价模型类型 iba_evaluate_type |
| 14 | fbillno | 报告编号 | varchar | 30 |  | √ | ' ' | 报告编号 |
| 15 | funit | 金额单位 | varchar | 50 |  | √ | ' ' | 金额单位,枚举: 1 :元 2 :万元 3 :亿元 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_iba_report_record |  | fid |
| 2 | idx_iba_report_record |  | fbillno |

---

## 对标公司-多选基础资料表 t_iba_report_compare_c

- **表名称：** 对标公司-多选基础资料表
- **表名：** t_iba_report_compare_c

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 上市公司 ipo_listed_company |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_iba_report_compare_c |  | fid |
| 2 | pk_iba_report_compare_c |  | fpkid |

---

## 附件-附件表 t_iba_report_record_file

- **表名称：** 附件-附件表
- **表名：** t_iba_report_record_file

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 附件字段实体 bd_attachment |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | FPKID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_iba_report_record_file |  | fpkid |
| 2 | idx_iba_report_record_file |  | fid |
