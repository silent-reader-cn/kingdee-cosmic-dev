# 立项单与项目模板公共单据-mpm_projecttplbill

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

## 交付物料-子表 t_mpm_pabpaybillen

- **表名称：** 交付物料-子表
- **表名：** t_mpm_pabpaybillen

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | finspectqty | 已验收数量 | numeric | 23 | 10 | √ | 0 | 已验收数量 |
| 3 | foutqty | 已出库数量 | numeric | 23 | 10 | √ | 0 | 已出库数量 |
| 4 | fsrcbillno | 源单编号 | varchar | 80 |  | √ | ' ' | 源单编号 |
| 5 | frelatebaseqty | 关联基本数量 | numeric | 23 | 10 | √ | 0 | 关联基本数量 |
| 6 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料销售信息 bd_materialsalinfo](../sbd_files/bd_materialsalinfo.md) |
| 7 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | famount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 10 | fprice | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 11 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 12 | fsrcbillformid | 来源单据实体 | varchar | 80 |  | √ | ' ' | 来源单据实体 |
| 13 | fauxunitid | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 14 | fproorgid | fproorgid | int8 | 64 |  | √ | 0 |  |
| 15 | fbondcontrol | 物料保税控制 | bpchar | 1 |  | √ | '0' | 物料保税控制,枚举: 0 :非保税 1 :保税 2 :不控制 |
| 16 | fcuramount | 金额(本位币) | numeric | 23 | 10 | √ | 0 | 金额(本位币) |
| 17 | fmaterialversionid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 18 | fauxunit2id | 辅助单位(2) | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 19 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 20 | frelateqty | 关联数量 | numeric | 23 | 10 | √ | 0 | 关联数量 |
| 21 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 22 | fpurorgid | fpurorgid | int8 | 64 |  | √ | 0 |  |
| 23 | fsrcbillseq | 源单行号 | int4 | 32 |  | √ | 0 | 源单行号 |
| 24 | fsrcbillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 25 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 26 | flicensenoid | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 27 | fdescription | 描述 | varchar | 512 |  |  | null | 描述 |
| 28 | fsrcbillentryid | 源单分录行ID | int8 | 64 |  | √ | 0 | 源单分录行ID |
| 29 | foutbaseqty | 已出库基本数量 | numeric | 23 | 10 | √ | 0 | 已出库基本数量 |
| 30 | fmaterialmasterid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 31 | fauxqty2 | 辅助数量(2) | numeric | 23 | 10 | √ | 0 | 辅助数量(2) |
| 32 | fauxqty | 辅助数量 | numeric | 23 | 10 | √ | 0 | 辅助数量 |
| 33 | fbaseinspectqty | 已验收基本数量 | numeric | 23 | 10 | √ | 0 | 已验收基本数量 |
| 34 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 35 | fenbizopregid | 商机号 | int8 | 64 |  | √ | 0 | [商机登记F7 mpm_bizopregf7](../mpm_files/mpm_bizopregf7.md) |
| 36 | fsupplyorgid | 供应组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 37 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 38 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | [行类型 bd_linetype](../sbd_files/bd_linetype.md) |
| 39 | fstockorgid | 发货组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 40 | fentrychangetype | 变更方式 | bpchar | 1 |  | √ | ' ' | 变更方式,枚举: A :新增 B :修改 C :删除 |
| 41 | fmaterialname | 物料名称(历史) | varchar | 512 |  |  | ' ' | 物料名称(历史) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpm_pabpaybillen_fid |  | fid |
| 2 | pk_mpm_pabpaybillen |  | fentryid |

---

## 关联父项目里程碑-子表 t_mpm_approvreltasken

- **表名称：** 关联父项目里程碑-子表
- **表名：** t_mpm_approvreltasken

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fparentporjtaskid | 父项目任务 | int8 | 64 |  | √ | 0 | [项目任务F7 mpm_task_f7](../mpm_files/mpm_task_f7.md) |
| 3 | freltaskchtype | 变更方式 | bpchar | 1 |  | √ | ' ' | 变更方式,枚举: A :新增 B :修改 C :删除 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fparentporjmilestoneid | 父项目里程碑 | int8 | 64 |  | √ | 0 | [项目任务 bd_projecttask](../basedata_files/bd_projecttask.md) |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpm_approvreltasken |  | fentryid |
| 2 | idx_mpm_appreltsken_msid |  | fparentporjmilestoneid |
| 3 | idx_mpm_apprreltaske_fk |  | fid |

---

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

## 立项单与项目模板公共单据-分表 t_mpm_projapprbil_a

- **表名称：** 立项单与项目模板公共单据-分表
- **表名：** t_mpm_projapprbil_a

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
| 1 | pk_mpm_projapprbil_a |  | fid |

---

## 立项单与项目模板公共单据-分表 t_mpm_projapprbil_c

- **表名称：** 立项单与项目模板公共单据-分表
- **表名：** t_mpm_projapprbil_c

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsubversion | 子版本号 | varchar | 50 |  | √ | ' ' | 子版本号 |
| 3 | fchangerid | 变更人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fchangedate | 变更日期 | timestamp | 0 |  |  | null | 变更日期 |
| 5 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fversion | 版本号 | varchar | 50 |  | √ | '1' | 版本号 |
| 7 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fchangestatus | 变更状态 | bpchar | 1 |  | √ | ' ' | 变更状态,枚举: A :正常 B :变更中 C :已变更 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpm_projapprbil_c |  | fid |

---

## 立项单与项目模板公共单据-分表 t_mpm_projapprbil_e

- **表名称：** 立项单与项目模板公共单据-分表
- **表名：** t_mpm_projapprbil_e

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
| 1 | pk_mpm_projapprbil_e |  | fid |

---

## 立项单与项目模板公共单据-主表 t_mpm_projapprbil

- **表名称：** 立项单与项目模板公共单据-主表
- **表名：** t_mpm_projapprbil

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | faddress | 联系地址 | varchar | 600 |  |  | null | 联系地址 |
| 3 | factualenddate | 实际完成日期 | timestamp | 0 |  |  | null | 实际完成日期 |
| 4 | fdeviationrate | 偏差率(%) | numeric | 23 | 10 | √ | 0 | 偏差率(%) |
| 5 | forgid | 业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fprocess | 进度(%) | numeric | 23 | 10 | √ | 0 | 进度(%) |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 9 | fexpectearn | 预计收益 | numeric | 23 | 10 | √ | 0 | 预计收益 |
| 10 | fcalendarid | 项目日历 | int8 | 64 |  | √ | 0 | [项目日历 mpm_calendar](../mpm_files/mpm_calendar.md) |
| 11 | fexpectrevenue | 预计收入 | numeric | 23 | 10 | √ | 0 | 预计收入 |
| 12 | fprojectno | 项目编码 | varchar | 80 |  | √ | ' ' | 项目编码 |
| 13 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 14 | fcurexpearn | 预计收益(本位币) | numeric | 23 | 10 | √ | 0 | 预计收益(本位币) |
| 15 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 16 | fplanenddate | 计划完成日期 | timestamp | 0 |  |  | null | 计划完成日期 |
| 17 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 18 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 19 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 20 | fexpectexpend | 预计支出 | numeric | 23 | 10 | √ | 0 | 预计支出 |
| 21 | factualbegindate | 实际开始日期 | timestamp | 0 |  |  | null | 实际开始日期 |
| 22 | fparentprojectid | 父项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 23 | fcurexpexpend | 预计支出(本位币) | numeric | 23 | 10 | √ | 0 | 预计支出(本位币) |
| 24 | fprojectname | 项目名称 | varchar | 255 |  | √ | ' ' | 项目名称 |
| 25 | fprojectkindid | 项目分类 | int8 | 64 |  | √ | 0 | [项目分类 bd_projectkind](../basedata_files/bd_projectkind.md) |
| 26 | fexchangetype | 换算方式 | varchar | 5 |  | √ | ' ' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 27 | flinkmanid | 联系人 | int8 | 64 |  | √ | 0 | [客户联系人 bd_customerlinkman](../sbd_files/bd_customerlinkman.md) |
| 28 | fsettleorgid | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 29 | fsettlecurrencyid | 结算币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 30 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 31 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 32 | fcustomerid | 订货客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 33 | foperatorid | 销售员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 34 | fplanbegindate | 计划开始日期 | timestamp | 0 |  |  | null | 计划开始日期 |
| 35 | fprojectmanagerid | 项目经理 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 36 | fcurexprevenue | 预计收入(本位币) | numeric | 23 | 10 | √ | 0 | 预计收入(本位币) |
| 37 | fsaledeptid | 销售部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 38 | frespdeptid | 负责部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 39 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 40 | fprojecttemplateid | 项目模板 | int8 | 64 |  | √ | 0 | [项目模板 mpm_projecttemplate](../mpm_files/mpm_projecttemplate.md) |
| 41 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 42 | fbizopregid | 商机号 | int8 | 64 |  | √ | 0 | [商机登记F7 mpm_bizopregf7](../mpm_files/mpm_bizopregf7.md) |
| 43 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 44 | foperatorgroupid | 销售组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 45 | fplanday | 计划工期(天) | numeric | 23 | 10 | √ | 0 | 计划工期(天) |
| 46 | fsaleorgid | 销售组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 47 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 48 | fprojectstatusid | 项目状态 | int8 | 64 |  | √ | 0 | [项目状态 bd_projectstatus](../basedata_files/bd_projectstatus.md) |
| 49 | fcurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpm_projapprbil_fbillno |  | fbillno |
| 2 | idx_mpm_projapprbil_fprj |  | fprojectid |
| 3 | pk_mpm_projapprbil |  | fid |

---

## 立项单与项目模板公共单据-多语言表 t_mpm_projapprbil_l

- **表名称：** 立项单与项目模板公共单据-多语言表
- **表名：** t_mpm_projapprbil_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fprojectname | 项目名称 | varchar | 255 |  | √ | ' ' | 项目名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpm_projapprbil_l |  | fid,flocaleid |
| 2 | pk_mpm_projapprbil_l |  | fpkid |

---

## 立项单与项目模板公共单据-分表 t_mpm_projapprbil_o

- **表名称：** 立项单与项目模板公共单据-分表
- **表名：** t_mpm_projapprbil_o

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fistemplate | 是否模板 | bpchar | 1 |  | √ | '0' | 是否模板 |
| 3 | fisgenplanfromtpl | 按模板生成计划 | bpchar | 1 |  | √ | '0' | 按模板生成计划 |
| 4 | fgenplanfrtplstat | 按模板生成计划状态 | bpchar | 1 |  | √ | 'A' | 按模板生成计划状态,枚举: A :未生成 B :已生成按计划 C :已生成未按计划 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpm_projapprbil_o |  | fid |

---

## 立项单与项目模板公共单据-关联追踪表 t_mpm_projapprbil_tc

- **表名称：** 立项单与项目模板公共单据-关联追踪表
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

## 立项单与项目模板公共单据-反写记录表 t_mpm_projapprbil_wb

- **表名称：** 立项单与项目模板公共单据-反写记录表
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
