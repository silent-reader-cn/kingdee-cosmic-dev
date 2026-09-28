# 行业方案设置-iba_org_report_scheme

## 行业方案设置-多语言表 t_iba_report_scheme_l

- **表名称：** 行业方案设置-多语言表
- **表名：** t_iba_report_scheme_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_iba_report_scheme_l |  | fid |
| 2 | pk_iba_report_scheme_l |  | fpkid |

---

## 行业方案设置-主表 t_iba_report_scheme

- **表名称：** 行业方案设置-主表
- **表名：** t_iba_report_scheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | frangenumber | 企业版合并方案范围编码 | varchar | 50 |  | √ | ' ' | 企业版合并方案范围编码 |
| 3 | forgfield | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fschemenumber | 企业版合并方案编码 | varchar | 50 |  | √ | ' ' | 企业版合并方案编码 |
| 5 | fpolicynumber | 会计政策编码 | varchar | 50 |  | √ | ' ' | 会计政策编码 |
| 6 | fstartperiod | 起始期 | varchar | 50 |  | √ | ' ' | 起始期 |
| 7 | frptitemgroup | 旗舰版报表项目分组 | int8 | 64 |  | √ | 0 | [报表项目分组 xkbd_rptitemgroup](../fibd_files/xkbd_rptitemgroup.md) |
| 8 | faccountingsysnumber | 核算体系编码 | varchar | 50 |  | √ | ' ' | 核算体系编码 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | freport_template | 合并报表模板 | varchar | 36 |  | √ | ' ' | [合并报表模板 xkcr_consdtrptsample](../xkcr_files/xkcr_consdtrptsample.md) |
| 14 | freporttype | 报表类型 | varchar | 50 |  | √ | ' ' | 报表类型,枚举: 0 :合并报表 1 :报表 |
| 15 | faccountbook_scheme | 合并账簿方案 | int8 | 64 |  | √ | 0 | [账簿合并方案 gl_bookscheme](../fmb_files/gl_bookscheme.md) |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fsyncperiod | 同步日期 | varchar | 50 |  | √ | ' ' | 同步日期 |
| 18 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | forgnumber | 组织编码 | varchar | 50 |  | √ | ' ' | 组织编码 |
| 21 | fipo_org | IPO主体 | int8 | 64 |  | √ | 0 | [IPO编制组织 ipo_org](../ipobase_files/ipo_org.md) |
| 22 | freport_scheme | 合并报表方案 | int8 | 64 |  | √ | 0 | [合并方案 xkcr_scopetype](../xkcr_files/xkcr_scopetype.md) |
| 23 | fdata_updatetime | 数据方案最后更新时间 | timestamp | 0 |  |  | null | 数据方案最后更新时间 |
| 24 | fpolicy | 会计政策 | int8 | 64 |  | √ | 0 | [会计政策 xkbd_policy](../fibd_files/xkbd_policy.md) |
| 25 | frptitemgroupnumber | 企业版分组编码 | varchar | 50 |  | √ | ' ' | 企业版分组编码 |
| 26 | faccountingsys | 核算体系 | int8 | 64 |  | √ | 0 | [核算体系 xkbd_accountingsys](../fibd_files/xkbd_accountingsys.md) |
| 27 | fperiod | 周期 | varchar | 50 |  | √ | ' ' | 周期 |
| 28 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 29 | fdatasource | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: flagship :星空旗舰 business :星空企业 other :其他系统 |
| 30 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 31 | fenbperiod | 结束期 | varchar | 50 |  | √ | ' ' | 结束期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_iba_report_scheme |  | fid |
| 2 | idx_iba_report_scheme |  | fipo_org |
