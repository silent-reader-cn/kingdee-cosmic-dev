# IPO主体报表方案-ipo_org_report_scheme

## IPO主体报表方案-主表 t_theme_report_scheme

- **表名称：** IPO主体报表方案-主表
- **表名：** t_theme_report_scheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | frangenumber | 企业版合并方案范围编码 | varchar | 50 |  | √ | ' ' | 企业版合并方案范围编码 |
| 3 | fschemenumber | 企业版合并方案编码 | varchar | 50 |  | √ | ' ' | 企业版合并方案编码 |
| 4 | fstartperiod | 起始期 | varchar | 50 |  | √ | ' ' | 起始期 |
| 5 | frptitemgroup | 旗舰版报表项目分组 | int8 | 64 |  |  | null | 报表项目分组 xkbd_rptitemgroup |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | freport_template | 合并报表模板 | varchar | 36 |  | √ | ' ' | 合并报表模板 xkcr_consdtrptsample |
| 11 | freporttype | 报表类型 | bpchar | 1 |  | √ | '0' | 报表类型,枚举: 0 :合并报表 1 :报表 |
| 12 | fappmake | 应用 | varchar | 50 |  | √ | '0' | 应用,枚举: 0 :IPO主题分析 1 :IPO上市智测 |
| 13 | faccountbook_scheme | 合并账簿方案 | int8 | 64 |  | √ | 0 | 账簿合并方案 gl_bookscheme |
| 14 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 16 | fsyncperiod | 同步日期 | varchar | 50 |  | √ | ' ' | 同步日期 |
| 17 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 18 | fipo_org | IPO主体 | int8 | 64 |  | √ | 0 | IPO编制组织 ipo_org |
| 19 | freport_scheme | 合并报表方案 | int8 | 64 |  | √ | 0 | 合并方案 xkcr_scopetype |
| 20 | fdata_updatetime | 数据方案最后更新时间 | timestamp | 0 |  |  | null | 数据方案最后更新时间 |
| 21 | frptitemgroupnumber | 企业版分组编码 | varchar | 50 |  | √ | ' ' | 企业版分组编码 |
| 22 | fperiod | 周期 | varchar | 50 |  | √ | ' ' | 周期 |
| 23 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 24 | fdatasource | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: flagship :星空旗舰 business :星空企业 other :其他系统 |
| 25 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 26 | fenbperiod | 结束期 | varchar | 50 |  | √ | ' ' | 结束期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_theme_report_scheme |  | fid |
| 2 | report_scheme_index |  | fipo_org |

---

## IPO主体报表方案-多语言表 t_theme_report_scheme_l

- **表名称：** IPO主体报表方案-多语言表
- **表名：** t_theme_report_scheme_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_theme_report_scheme_l_0 |  | fid |
| 2 | pk_theme_report_scheme_l |  | fpkid |
