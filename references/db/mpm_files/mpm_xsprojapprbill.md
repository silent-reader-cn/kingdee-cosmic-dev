# 项目变更单-mpm_xsprojapprbill

## 关联子实体-子表 t_mpm_pabpaybillen_lk

- **表名称：** 关联子实体-子表
- **表名：** t_mpm_pabpaybillen_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpm_pabpaybillen_lk |  | fpkid |
| 2 | idx_mpm_pabpaybillen_lk_fk |  | fentryid |

---

## 项目变更单-多语言表 t_mpm_xsprojapprbl_l

- **表名称：** 项目变更单-多语言表
- **表名：** t_mpm_xsprojapprbl_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fprojectname | 项目名称 | varchar | 255 |  | √ | ' ' | 项目名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | freason | 变更原因 | varchar | 512 |  | √ | ' ' | 变更原因 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpm_xsprojapprbl_l |  | fpkid |
| 2 | idx_mpm_xsprojapprbl_l |  | fid,flocaleid |

---

## 项目变更单-分表 t_mpm_xsprojapprbl_a

- **表名称：** 项目变更单-分表
- **表名：** t_mpm_xsprojapprbl_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fprojectdesc_tag | 项目描述大文本_详情 | text | 0 |  |  | ' ' | 项目描述大文本_详情 |
| 3 | fprojectdesc | 项目描述大文本 | text | 0 |  |  | ' ' | 项目描述大文本 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpm_xsprojapprbl_a |  | fid |

---

## 项目变更单-分表 t_mpm_xsprojapprbl_c

- **表名称：** 项目变更单-分表
- **表名：** t_mpm_xsprojapprbl_c

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | factivedate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 3 | factivestatus | 生效状态 | bpchar | 1 |  | √ | ' ' | 生效状态,枚举: A :未生效 B :已生效 |
| 4 | fsourcebillentity | 源单实体 | varchar | 80 |  | √ | ' ' | 源单实体 |
| 5 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fchangebizdate | 变更单日期 | timestamp | 0 |  |  | null | 变更单日期 |
| 7 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fchangestatus | 变更状态 | bpchar | 1 |  | √ | ' ' | 变更状态,枚举: A :正常 B :变更中 C :已变更 |
| 9 | fchangebillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 10 | fsubversion | 子版本号 | varchar | 50 |  | √ | ' ' | 子版本号 |
| 11 | factiverid | 生效人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fsrcbillstatus | 立项单状态 | bpchar | 1 |  | √ | ' ' | 立项单状态,枚举: A :创建 B :审核中 C :已审核 D :重新审核 |
| 13 | fchangerid | 变更人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fchangedate | 变更日期 | timestamp | 0 |  |  | null | 变更日期 |
| 15 | fsourcebillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 16 | fversion | 版本号 | varchar | 50 |  | √ | '1' | 版本号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpm_xspjappr_fchblno |  | fchangebillno |
| 2 | pk_mpm_xsprojapprbl_c |  | fid |

---

## 项目变更单-分表 t_mpm_xsprojapprbl_e

- **表名称：** 项目变更单-分表
- **表名：** t_mpm_xsprojapprbl_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcustfield031 | 自定义复选框001 | bpchar | 1 |  | √ | '0' | 自定义复选框001 |
| 3 | fcustfield030 | 自定义日期005 | timestamp | 0 |  |  | null | 自定义日期005 |
| 4 | fcustfield011 | 自定义文本011 | varchar | 80 |  | √ | ' ' | 自定义文本011 |
| 5 | fcustfield033 | 自定义复选框003 | bpchar | 1 |  | √ | '0' | 自定义复选框003 |
| 6 | fcustfield010 | 自定义文本010 | varchar | 80 |  | √ | ' ' | 自定义文本010 |
| 7 | fcustfield032 | 自定义复选框002 | bpchar | 1 |  | √ | '0' | 自定义复选框002 |
| 8 | fcustfield017 | 自定义文本017 | varchar | 80 |  | √ | ' ' | 自定义文本017 |
| 9 | fcustfield016 | 自定义文本016 | varchar | 80 |  | √ | ' ' | 自定义文本016 |
| 10 | fcustfield019 | 自定义文本019 | varchar | 80 |  | √ | ' ' | 自定义文本019 |
| 11 | fcustfield018 | 自定义文本018 | varchar | 80 |  | √ | ' ' | 自定义文本018 |
| 12 | fcustfield013 | 自定义文本013 | varchar | 80 |  | √ | ' ' | 自定义文本013 |
| 13 | fcustfield035 | 自定义复选框005 | bpchar | 1 |  | √ | '0' | 自定义复选框005 |
| 14 | fcustfield012 | 自定义文本012 | varchar | 80 |  | √ | ' ' | 自定义文本012 |
| 15 | fcustfield034 | 自定义复选框004 | bpchar | 1 |  | √ | '0' | 自定义复选框004 |
| 16 | fcustfield015 | 自定义文本015 | varchar | 80 |  | √ | ' ' | 自定义文本015 |
| 17 | fcustfield014 | 自定义文本014 | varchar | 80 |  | √ | ' ' | 自定义文本014 |
| 18 | fcustfield020 | 自定义文本020 | varchar | 80 |  | √ | ' ' | 自定义文本020 |
| 19 | fcustfield022 | 自定义数字002 | numeric | 23 | 10 | √ | 0 | 自定义数字002 |
| 20 | fcustfield021 | 自定义数字001 | numeric | 23 | 10 | √ | 0 | 自定义数字001 |
| 21 | fcustfield009 | 自定义文本009 | varchar | 80 |  | √ | ' ' | 自定义文本009 |
| 22 | fcustfield006 | 自定义文本006 | varchar | 80 |  | √ | ' ' | 自定义文本006 |
| 23 | fcustfield028 | 自定义日期003 | timestamp | 0 |  |  | null | 自定义日期003 |
| 24 | fcustfield005 | 自定义文本005 | varchar | 80 |  | √ | ' ' | 自定义文本005 |
| 25 | fcustfield027 | 自定义日期002 | timestamp | 0 |  |  | null | 自定义日期002 |
| 26 | fcustfield008 | 自定义文本008 | varchar | 80 |  | √ | ' ' | 自定义文本008 |
| 27 | fcustfield007 | 自定义文本007 | varchar | 80 |  | √ | ' ' | 自定义文本007 |
| 28 | fcustfield029 | 自定义日期004 | timestamp | 0 |  |  | null | 自定义日期004 |
| 29 | fcustfield002 | 自定义文本002 | varchar | 80 |  | √ | ' ' | 自定义文本002 |
| 30 | fcustfield024 | 自定义数字004 | numeric | 23 | 10 | √ | 0 | 自定义数字004 |
| 31 | fcustfield001 | 自定义文本001 | varchar | 80 |  | √ | ' ' | 自定义文本001 |
| 32 | fcustfield023 | 自定义数字003 | numeric | 23 | 10 | √ | 0 | 自定义数字003 |
| 33 | fcustfield004 | 自定义文本004 | varchar | 80 |  | √ | ' ' | 自定义文本004 |
| 34 | fcustfield026 | 自定义日期001 | timestamp | 0 |  |  | null | 自定义日期001 |
| 35 | fcustfield003 | 自定义文本003 | varchar | 80 |  | √ | ' ' | 自定义文本003 |
| 36 | fcustfield025 | 自定义数字005 | numeric | 23 | 10 | √ | 0 | 自定义数字005 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpm_xsprojapprbl_e |  | fid |

---

## 项目变更单-主表 t_mpm_xsprojapprbl

- **表名称：** 项目变更单-主表
- **表名：** t_mpm_xsprojapprbl

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | faddress | 联系地址 | varchar | 600 |  |  | null | 联系地址 |
| 3 | factualenddate | 实际完成日期 | timestamp | 0 |  |  | null | 实际完成日期 |
| 4 | fdeviationrate | 偏差率(%) | numeric | 23 | 10 | √ | 0 | 偏差率(%) |
| 5 | forgid | 业务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fprocess | 进度(%) | numeric | 23 | 10 | √ | 0 | 进度(%) |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 9 | fexpectearn | 预计收益 | numeric | 23 | 10 | √ | 0 | 预计收益 |
| 10 | fcalendarid | 项目日历 | int8 | 64 |  | √ | 0 | 项目日历 mpm_calendar |
| 11 | fexpectrevenue | 预计收入 | numeric | 23 | 10 | √ | 0 | 预计收入 |
| 12 | fprojectno | 项目编码 | varchar | 80 |  | √ | ' ' | 项目编码 |
| 13 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | 汇率表 bd_exratetable |
| 14 | fcurexpearn | 预计收益(本位币) | numeric | 23 | 10 | √ | 0 | 预计收益(本位币) |
| 15 | fbillno | 立项单编号 | varchar | 80 |  | √ | ' ' | 立项单编号 |
| 16 | fplanenddate | 计划完成日期 | timestamp | 0 |  |  | null | 计划完成日期 |
| 17 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 18 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 19 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 20 | freason | 变更原因 | varchar | 512 |  | √ | ' ' | 变更原因 |
| 21 | fexpectexpend | 预计支出 | numeric | 23 | 10 | √ | 0 | 预计支出 |
| 22 | factualbegindate | 实际开始日期 | timestamp | 0 |  |  | null | 实际开始日期 |
| 23 | fparentprojectid | 父项目 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 24 | fcurexpexpend | 预计支出(本位币) | numeric | 23 | 10 | √ | 0 | 预计支出(本位币) |
| 25 | fprojectname | 项目名称 | varchar | 255 |  | √ | ' ' | 项目名称 |
| 26 | fprojectkindid | 项目分类 | int8 | 64 |  | √ | 0 | 项目分类 bd_projectkind |
| 27 | fexchangetype | 换算方式 | varchar | 5 |  | √ | ' ' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 28 | flinkmanid | 联系人 | int8 | 64 |  |  | null | 客户联系人 bd_customerlinkman |
| 29 | fsettleorgid | 结算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 30 | fsettlecurrencyid | 结算币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 31 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 32 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 33 | fcustomerid | 订货客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 34 | foperatorid | 销售员 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 35 | fplanbegindate | 计划开始日期 | timestamp | 0 |  |  | null | 计划开始日期 |
| 36 | fprojectmanagerid | 项目经理 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 37 | fcurexprevenue | 预计收入(本位币) | numeric | 23 | 10 | √ | 0 | 预计收入(本位币) |
| 38 | fsaledeptid | 销售部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 39 | frespdeptid | 负责部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 40 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 41 | fprojecttemplateid | 项目模板 | int8 | 64 |  | √ | 0 | 项目模板 mpm_projecttemplate |
| 42 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 43 | fbizopregid | 商机号 | int8 | 64 |  | √ | 0 | 商机登记F7 mpm_bizopregf7 |
| 44 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 45 | foperatorgroupid | 销售组 | int8 | 64 |  | √ | 0 | 供应链业务组 bd_operatorgroup |
| 46 | fplanday | 计划工期(天) | numeric | 23 | 10 | √ | 0 | 计划工期(天) |
| 47 | fsaleorgid | 销售组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 48 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 49 | fprojectstatusid | 项目状态 | int8 | 64 |  | √ | 0 | 项目状态 bd_projectstatus |
| 50 | fcurrencyid | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpm_xsprojapprbl |  | fid |
| 2 | idx_mpm_xspjappr_fbillno |  | fbillno |

---

## 关联子实体-子表 t_mpm_projapprbil_lk

- **表名称：** 关联子实体-子表
- **表名：** t_mpm_projapprbil_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpm_projapprbil_lk_fk |  | fid |
| 2 | pk_mpm_projapprbil_lk |  | fpkid |

---

## 交付物料-子表 t_mpm_xspabpayblen

- **表名称：** 交付物料-子表
- **表名：** t_mpm_xspabpayblen

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | finspectqty | 已验收数量 | numeric | 23 | 10 | √ | 0 | 已验收数量 |
| 3 | foutqty | 已出库数量 | numeric | 23 | 10 | √ | 0 | 已出库数量 |
| 4 | fsrcentryid | 立项单分录ID | int8 | 64 |  | √ | 0 | 立项单分录ID |
| 5 | fsrcbillno | 源单编号 | varchar | 80 |  | √ | ' ' | 源单编号 |
| 6 | frelatebaseqty | 关联基本数量 | numeric | 23 | 10 | √ | 0 | 关联基本数量 |
| 7 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料销售信息 bd_materialsalinfo |
| 8 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 9 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 10 | famount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 11 | fprice | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 12 | fauxunitid | 辅助单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 13 | fsrcbillformid | 来源单据实体 | varchar | 80 |  | √ | ' ' | 来源单据实体 |
| 14 | fcuramount | 金额(本位币) | numeric | 23 | 10 | √ | 0 | 金额(本位币) |
| 15 | fmaterialversionid | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 16 | fauxunit2id | 辅助单位(2) | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 17 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 18 | frelateqty | 关联数量 | numeric | 23 | 10 | √ | 0 | 关联数量 |
| 19 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 20 | fsrcbillseq | 源单行号 | int4 | 32 |  | √ | 0 | 源单行号 |
| 21 | fsrcbillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 22 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 23 | fdescription | 描述 | varchar | 512 |  |  | null | 描述 |
| 24 | fsrcbillentryid | 源单分录行ID | int8 | 64 |  | √ | 0 | 源单分录行ID |
| 25 | foutbaseqty | 已出库基本数量 | numeric | 23 | 10 | √ | 0 | 已出库基本数量 |
| 26 | fmaterialmasterid | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 27 | fauxqty2 | 辅助数量(2) | numeric | 23 | 10 | √ | 0 | 辅助数量(2) |
| 28 | fauxqty | 辅助数量 | numeric | 23 | 10 | √ | 0 | 辅助数量 |
| 29 | fbaseinspectqty | 已验收基本数量 | numeric | 23 | 10 | √ | 0 | 已验收基本数量 |
| 30 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 31 | fenbizopregid | 商机号 | int8 | 64 |  | √ | 0 | 商机登记F7 mpm_bizopregf7 |
| 32 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 33 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | 行类型 bd_linetype |
| 34 | fstockorgid | 发货组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 35 | fentrychangetype | 变更方式 | bpchar | 1 |  | √ | ' ' | 变更方式,枚举: A :新增 B :修改 C :删除 |
| 36 | fmaterialname | 物料名称(历史) | varchar | 512 |  |  | ' ' | 物料名称(历史) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpm_xspabpayblen_fid |  | fid |
| 2 | pk_mpm_xspabpayblen |  | fentryid |

---

## 项目变更单-关联追踪表 t_mpm_projapprbil_tc

- **表名称：** 项目变更单-关联追踪表
- **表名：** t_mpm_projapprbil_tc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | ftbillid | ftbillid | int8 | 64 |  |  | null |  |
| 3 | fttableid | fttableid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | ftid | ftid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpm_projapprbil_tc_tid |  | ftid |
| 2 | idx_mpm_projapprbil_tc_tbill |  | ftbillid |
| 3 | pk_mpm_projapprbil_tc |  | fid |

---

## 项目变更单-反写记录表 t_mpm_projapprbil_wb

- **表名称：** 项目变更单-反写记录表
- **表名：** t_mpm_projapprbil_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | foperate | foperate | varchar | 50 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 |  | null |  |
| 8 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpm_projapprbil_wb |  | fentryid |
| 2 | idx_mpm_projapprbil_wb_fk |  | fid |
