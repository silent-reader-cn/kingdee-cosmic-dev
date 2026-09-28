# 外部数据监控库-pbd_supplier_data

## 抽查检查-子表 t_pbd_smoni_checkentity

- **表名称：** 抽查检查-子表
- **表名：** t_pbd_smoni_checkentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 1024 |  | √ | ' ' | 备注 |
| 3 | fcheckresult | 结果 | varchar | 255 |  | √ | ' ' | 结果 |
| 4 | fupdatetime | 更新日期 | timestamp | 0 |  |  | null | 更新日期 |
| 5 | fcheckresult_tag | 结果_详情 | text | 0 |  |  | null | 结果_详情 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fcheckid | 合作方ID | int8 | 64 |  | √ | 0 | 合作方ID |
| 8 | fcheckdate | 日期 | timestamp | 0 |  |  | null | 日期 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fcheckorg | 检查实施机关 | varchar | 100 |  | √ | ' ' | 检查实施机关 |
| 11 | fchecktype | 类型 | varchar | 10 |  | √ | ' ' | 类型 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pbd_smoni_checkentity |  | fentryid |
| 2 | idx_pbd_smoni_check_fid_fseq |  | fid,fseq |

---

## 外部数据监控库-关联追踪表 t_pbd_smoni_data_tc

- **表名称：** 外部数据监控库-关联追踪表
- **表名：** t_pbd_smoni_data_tc

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
| 1 | pk_pbd_smoni_data_tc |  | fid |
| 2 | idx_pbd_smoni_data_tc_tbill |  | ftbillid |
| 3 | idx_pbd_smoni_data_tc_tid |  | ftid |

---

## 严重违法-子表 t_pbd_smoni_illegalentity

- **表名称：** 严重违法-子表
- **表名：** t_pbd_smoni_illegalentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremovedepartment | 移出机关 | varchar | 200 |  | √ | ' ' | 移出机关 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fputdepartment | 决定列入部门 | varchar | 200 |  | √ | ' ' | 决定列入部门 |
| 5 | fillegalid | 合作方Id | int8 | 64 |  | √ | 0 | 合作方Id |
| 6 | fremovereason_tag | 移出原因_详情 | text | 0 |  |  | null | 移出原因_详情 |
| 7 | fremovereason | 移出原因 | varchar | 255 |  | √ | ' ' | 移出原因 |
| 8 | fputreason_tag | 列入原因_详情 | text | 0 |  |  | null | 列入原因_详情 |
| 9 | fupdatetime | 更新日期 | timestamp | 0 |  |  | null | 更新日期 |
| 10 | fputreason | 列入原因 | varchar | 255 |  | √ | ' ' | 列入原因 |
| 11 | fremovedate | 移出日期 | timestamp | 0 |  |  | null | 移出日期 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | fputdate | 列入日期 | timestamp | 0 |  |  | null | 列入日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pbd_smoni_illegalentity |  | fentryid |
| 2 | idx_pbd_smoni_illegal_fid_fseq |  | fid,fseq |

---

## 分支机构-子表 t_pbd_smoni_branchentity

- **表名称：** 分支机构-子表
- **表名：** t_pbd_smoni_branchentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbranchname | 分支机构名称 | varchar | 255 |  | √ | ' ' | 分支机构名称 |
| 3 | flegalpersonname | 法人 | varchar | 100 |  | √ | ' ' | 法人 |
| 4 | fregstatus | 企业状态 | varchar | 50 |  | √ | ' ' | 企业状态 |
| 5 | festiblishtime | 成立时间 | timestamp | 0 |  |  | null | 成立时间 |
| 6 | fbranchid | ID | int8 | 64 |  | √ | 0 | ID |
| 7 | fupdatetime | 更新日期 | timestamp | 0 |  |  | null | 更新日期 |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fbranchgid | 分支机构gid | int8 | 64 |  | √ | 0 | 分支机构gid |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pbd_smoni_branch_fid_fseq |  | fid,fseq |
| 2 | pk_pbd_smoni_branchentity |  | fentryid |

---

## 行政处罚【工商局】-子表 t_pbd_smoni_punishentity

- **表名称：** 行政处罚【工商局】-子表
- **表名：** t_pbd_smoni_punishentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | fdescription | 描述 | varchar | 100 |  | √ | ' ' | 描述 |
| 4 | fpublishid | 合作方Id | int8 | 64 |  | √ | 0 | 合作方Id |
| 5 | fpunishtype | 违法行为类型 | varchar | 100 |  | √ | ' ' | 违法行为类型 |
| 6 | fcontent_tag | 处罚结果/内容_详情 | text | 0 |  |  | null | 处罚结果/内容_详情 |
| 7 | fupdatetime | 更新日期 | timestamp | 0 |  |  | null | 更新日期 |
| 8 | fdecisiondate | 决定日期 | timestamp | 0 |  |  | null | 决定日期 |
| 9 | fdepartmentname | 决定机关 | varchar | 100 |  | √ | ' ' | 决定机关 |
| 10 | fpublishdate | 公示日期 | timestamp | 0 |  |  | null | 公示日期 |
| 11 | fcontent | 处罚结果/内容 | varchar | 255 |  | √ | ' ' | 处罚结果/内容 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | fpunishnumber | 定书文号 | varchar | 500 |  | √ | ' ' | 定书文号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pbd_smoni_punish_fid_fseq |  | fid,fseq |
| 2 | pk_pbd_smoni_punishentity |  | fentryid |

---

## 开庭公告-子表 t_pbd_smoni_ktanentity

- **表名称：** 开庭公告-子表
- **表名：** t_pbd_smoni_ktanentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fktdefendant | 被告 | varchar | 255 |  | √ | ' ' | 被告 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fktlitigant | 当事人 | varchar | 1000 |  | √ | ' ' | 当事人 |
| 5 | fktcourtroom | 法庭 | varchar | 50 |  | √ | ' ' | 法庭 |
| 6 | fktcourt | 法院 | varchar | 200 |  | √ | ' ' | 法院 |
| 7 | fktcaseno | 案号 | varchar | 50 |  | √ | ' ' | 案号 |
| 8 | fktcourtregreason | 案由 | varchar | 200 |  | √ | ' ' | 案由 |
| 9 | fktdefendant_tag | 被告_详情 | text | 0 |  |  | null | 被告_详情 |
| 10 | fktplaintiff | 原告 | varchar | 255 |  | √ | ' ' | 原告 |
| 11 | fupdatetime | 更新日期 | timestamp | 0 |  |  | null | 更新日期 |
| 12 | fktjudge | 审判长/主审人 | varchar | 200 |  | √ | ' ' | 审判长/主审人 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 14 | fktannouncementid | 合作方Id | int8 | 64 |  | √ | 0 | 合作方Id |
| 15 | fktdate | 开庭日期 | timestamp | 0 |  |  | null | 开庭日期 |
| 16 | fktplaintiff_tag | 原告_详情 | text | 0 |  |  | null | 原告_详情 |
| 17 | fktcontractors | 承办部门 | varchar | 200 |  | √ | ' ' | 承办部门 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pbd_smoni_ktan_fid_fseq |  | fid,fseq |
| 2 | pk_pbd_smoni_ktanentity |  | fentryid |

---

## 工商基本信息-子表 t_pbd_smoni_basicentity

- **表名称：** 工商基本信息-子表
- **表名：** t_pbd_smoni_basicentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 公司名称 | varchar | 255 |  | √ | ' ' | 公司名称 |
| 3 | flegalpersonname | 法人代表 | varchar | 255 |  | √ | ' ' | 法人代表 |
| 4 | fregstatus | 经营状态 | varchar | 50 |  | √ | ' ' | 经营状态 |
| 5 | fbasicinfoid | 合作方ID | int8 | 64 |  | √ | 0 | 合作方ID |
| 6 | foperatingperiodto | 营业期限至 | timestamp | 0 |  |  | null | 营业期限至 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fapprovedtime | 核准日期 | timestamp | 0 |  |  | null | 核准日期 |
| 9 | fbelongorg | 所属工商局 | varchar | 100 |  | √ | ' ' | 所属工商局 |
| 10 | fregcapital | 注册资本 | varchar | 50 |  | √ | ' ' | 注册资本 |
| 11 | fbusinessscope | 经营范围 | varchar | 255 |  | √ | ' ' | 经营范围 |
| 12 | foperatingperiodfrom | 营业期限始 | timestamp | 0 |  |  | null | 营业期限始 |
| 13 | fcurrencyunit | 货币单位 | varchar | 20 |  | √ | ' ' | 货币单位 |
| 14 | fupdatetime | 更新日期 | timestamp | 0 |  |  | null | 更新日期 |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 16 | fcompanyorgtype | 企业类型 | varchar | 255 |  | √ | ' ' | 企业类型 |
| 17 | fbusinessscope_tag | 经营范围_详情 | text | 0 |  |  | null | 经营范围_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pbd_smoni_basic_fid_fseq |  | fid,fseq |
| 2 | pk_pbd_smoni_basicentity |  | fentryid |

---

## 关联子实体-子表 t_pbd_smoni_data_lk

- **表名称：** 关联子实体-子表
- **表名：** t_pbd_smoni_data_lk

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
| 1 | pk_pbd_smoni_data_lk |  | fpkid |
| 2 | idx_pbd_smoni_data_lk_fk |  | fid |

---

## 新闻舆情-子表 t_pbd_smoni_newsentity

- **表名称：** 新闻舆情-子表
- **表名：** t_pbd_smoni_newsentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fnewssource | 新闻来源 | varchar | 255 |  | √ | ' ' | 新闻来源 |
| 3 | fupdatetime | 更新日期 | timestamp | 0 |  |  | null | 更新日期 |
| 4 | fnewstitle | 新闻标题 | varchar | 200 |  | √ | ' ' | 新闻标题 |
| 5 | fnewsurl | 新闻URL | varchar | 300 |  | √ | ' ' | 新闻URL |
| 6 | fnewsemotion | 新闻分类 | varchar | 50 |  | √ | ' ' | 新闻分类,枚举: 1 :正面 0 :中性 -1 :负面 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fdocid | 新闻唯一标识符 | varchar | 255 |  | √ | ' ' | 新闻唯一标识符 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pbd_smoni_newsentity |  | fentryid |
| 2 | idx_pbd_smoni_news_fid_fseq |  | fid,fseq |

---

## 外部数据监控库-主表 t_pbd_smoni_data

- **表名称：** 外部数据监控库-主表
- **表名：** t_pbd_smoni_data

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fillegalinfototal | 严重违法总数 | int4 | 32 |  | √ | 0 | 严重违法总数 |
| 3 | fexecuteetotal | 被执行人总数 | int4 | 32 |  | √ | 0 | 被执行人总数 |
| 4 | forgid | 审批组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fcompanychecktotal | 抽查检查总数 | int4 | 32 |  | √ | 0 | 抽查检查总数 |
| 6 | fpunishtotal | 行政处罚总数(工商局) | int4 | 32 |  | √ | 0 | 行政处罚总数(工商局) |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fcompanygid | 供应商ID | int8 | 64 |  | √ | 0 | 供应商ID |
| 10 | fdishonesttotal | 失信人总数 | int4 | 32 |  | √ | 0 | 失信人总数 |
| 11 | fmonitoraftertime | 监控结束时间 | timestamp | 0 |  |  | null | 监控结束时间 |
| 12 | fabntotal | 经营异常总数 | int4 | 32 |  | √ | 0 | 经营异常总数 |
| 13 | fcompanytotal | 工商变更总数 | int4 | 32 |  | √ | 0 | 工商变更总数 |
| 14 | fcourtregistertotal | 立案总数 | int4 | 32 |  | √ | 0 | 立案总数 |
| 15 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 16 | fremark | 备注 | varchar | 2000 |  | √ | ' ' | 备注 |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fholdertotal | 股权变更总数 | int4 | 32 |  | √ | 0 | 股权变更总数 |
| 19 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 20 | fbigsharetotal | 大股东变更总数 | int4 | 32 |  | √ | 0 | 大股东变更总数 |
| 21 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 22 | fmonitorbeforetime | 监控开始时间 | timestamp | 0 |  |  | null | 监控开始时间 |
| 23 | fsuppliername | 供应商名称 | varchar | 255 |  | √ | ' ' | 供应商名称 |
| 24 | fsuppliermonitorid | 监控池ID | int8 | 64 |  | √ | 0 | 监控池ID |
| 25 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 26 | fmonitorstatus | 监控状态 | bpchar | 1 |  | √ | ' ' | 监控状态,枚举: A :未监控 B :监控中 C :停止监控 |
| 27 | fnewstotal | 新闻总数 | int4 | 32 |  | √ | 0 | 新闻总数 |
| 28 | fbranchtotal | 分支机构总数 | int4 | 32 |  | √ | 0 | 分支机构总数 |
| 29 | fktannouncementtotal | 开庭总数 | int4 | 32 |  | √ | 0 | 开庭总数 |
| 30 | feid | 公司Id | varchar | 100 |  | √ | ' ' | 公司Id |
| 31 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 32 | fopunishtotal | 行政处罚总数(其他) | int4 | 32 |  | √ | 0 | 行政处罚总数(其他) |
| 33 | fcourtannototal | 法院公告总数 | int4 | 32 |  | √ | 0 | 法院公告总数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pbd_smoni_data_fcreattime |  | fcreatetime |
| 2 | pk_pbd_smoni_data |  | fid |
| 3 | idx_pbd_smoni_data_fbillno |  | fbillno |

---

## 经营异常-子表 t_pbd_smoni_abnentity

- **表名称：** 经营异常-子表
- **表名：** t_pbd_smoni_abnentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fadbid | 合作方Id | int8 | 64 |  | √ | 0 | 合作方Id |
| 3 | fremovedepartment | 移出机关 | varchar | 200 |  | √ | ' ' | 移出机关 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fputdepartment | 列入部门 | varchar | 200 |  | √ | ' ' | 列入部门 |
| 6 | fabnremovereason | 移出原因 | varchar | 255 |  | √ | ' ' | 移出原因 |
| 7 | fabnremovereason_tag | 移出原因_详情 | text | 0 |  |  | null | 移出原因_详情 |
| 8 | fupdatetime | 更新日期 | timestamp | 0 |  |  | null | 更新日期 |
| 9 | fremovedate | 移出日期 | timestamp | 0 |  |  | null | 移出日期 |
| 10 | fabnputreason_tag | 列入原因_详情 | text | 0 |  |  | null | 列入原因_详情 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 12 | fputdate | 列入日期 | timestamp | 0 |  |  | null | 列入日期 |
| 13 | fabnputreason | 列入原因 | varchar | 255 |  | √ | ' ' | 列入原因 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pbd_smoni_abn_fid_fseq |  | fid,fseq |
| 2 | pk_pbd_smoni_abnentity |  | fentryid |

---

## 工商变更-子表 t_pbd_smoni_comentity

- **表名称：** 工商变更-子表
- **表名：** t_pbd_smoni_comentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcompanyafter | 变更后 | varchar | 255 |  | √ | ' ' | 变更后 |
| 3 | fcompanybefore_tag | 变更前_详情 | text | 0 |  |  | null | 变更前_详情 |
| 4 | fupdatetime | 更新日期 | timestamp | 0 |  |  | null | 更新日期 |
| 5 | fchangetime | 变更时间 | timestamp | 0 |  |  | null | 变更时间 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fcompanybefore | 变更前 | varchar | 255 |  | √ | ' ' | 变更前 |
| 8 | fcompanyafter_tag | 变更后_详情 | text | 0 |  |  | null | 变更后_详情 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fcompanyitem_tag | 变更事项_详情 | text | 0 |  |  | null | 变更事项_详情 |
| 11 | fcompanyitem | 变更事项 | varchar | 255 |  | √ | ' ' | 变更事项 |
| 12 | fcompanyid | 合作方ID | int8 | 64 |  | √ | 0 | 合作方ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pbd_smoni_comentity |  | fentryid |
| 2 | idx_pbd_smoni_com_fid_fseq |  | fid,fseq |

---

## 失信被执行人-子表 t_pbd_smoni_dishoneentity

- **表名称：** 失信被执行人-子表
- **表名：** t_pbd_smoni_dishoneentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fperformance | 履行情况 | varchar | 200 |  | √ | ' ' | 履行情况 |
| 3 | fdishonestid | 合作方Id | int8 | 64 |  | √ | 0 | 合作方Id |
| 4 | fbusientity | 法人、负责人姓名 | varchar | 255 |  | √ | ' ' | 法人、负责人姓名 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fregdate | 立案日期 | timestamp | 0 |  |  | null | 立案日期 |
| 7 | fcaseno | 案号 | varchar | 50 |  | √ | ' ' | 案号 |
| 8 | fdishonestduty | 生效法律文书确定的义务 | varchar | 200 |  | √ | ' ' | 生效法律文书确定的义务 |
| 9 | fupdatetime | 更新日期 | timestamp | 0 |  |  | null | 更新日期 |
| 10 | fgistid | 执行依据文号 | varchar | 200 |  | √ | ' ' | 执行依据文号 |
| 11 | fdishonestgistunit | 做出执行的依据单位 | varchar | 200 |  | √ | ' ' | 做出执行的依据单位 |
| 12 | fpublishdate | 发布日期 | timestamp | 0 |  |  | null | 发布日期 |
| 13 | fdishonestcourt | 法院 | varchar | 200 |  | √ | ' ' | 法院 |
| 14 | fdisrupttypename | 失信被执行人行为具体情形 | varchar | 2000 |  | √ | ' ' | 失信被执行人行为具体情形 |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 16 | fdishonestiname | 失信人名称 | varchar | 255 |  | √ | ' ' | 失信人名称 |
| 17 | fareaname | 省份地区 | varchar | 200 |  | √ | ' ' | 省份地区 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pbd_smoni_dishoneentity |  | fentryid |
| 2 | idx_pbd_smoni_dishone_fid_fseq |  | fid,fseq |

---

## 大股东变更-子表 t_pbd_smoni_bigsharentity

- **表名称：** 大股东变更-子表
- **表名：** t_pbd_smoni_bigsharentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fholder | 现大股东名称 | varchar | 255 |  | √ | ' ' | 现大股东名称 |
| 3 | fholderid | ID | int8 | 64 |  | √ | 0 | ID |
| 4 | fholderbefore | 原大股东名称 | varchar | 255 |  | √ | ' ' | 原大股东名称 |
| 5 | fupdatetime | 更新日期 | timestamp | 0 |  |  | null | 更新日期 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pbd_smoni_bigsharentity |  | fentryid |
| 2 | idx_pbd_smoni_bigshar_fid_fseq |  | fid,fseq |

---

## 立案信息-子表 t_pbd_smoni_courtreentity

- **表名称：** 立案信息-子表
- **表名：** t_pbd_smoni_courtreentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcourtregid | 合作方Id | int8 | 64 |  | √ | 0 | 合作方Id |
| 3 | fcourtregstarttime | 开庭日期 | timestamp | 0 |  |  | null | 开庭日期 |
| 4 | fcourtregdefendant | 被告 | varchar | 255 |  | √ | ' ' | 被告 |
| 5 | fcourtregcasetype | 案件类型 | varchar | 200 |  | √ | ' ' | 案件类型 |
| 6 | fcourtregthird | 第三人 | varchar | 255 |  | √ | ' ' | 第三人 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fcourtregplaintiff | 原告 | varchar | 255 |  | √ | ' ' | 原告 |
| 9 | fcourtregcourt | 法院 | varchar | 200 |  | √ | ' ' | 法院 |
| 10 | fcourtregdepartment | 承办部门 | varchar | 200 |  | √ | ' ' | 承办部门 |
| 11 | fcourtregclosedate | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 12 | fcasestatus | 案件状态 | varchar | 200 |  | √ | ' ' | 案件状态 |
| 13 | fupdatetime | 更新日期 | timestamp | 0 |  |  | null | 更新日期 |
| 14 | fcourtregassistant | 法官助理 | varchar | 200 |  | √ | ' ' | 法官助理 |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 16 | ffilingdate | 立案日期 | timestamp | 0 |  |  | null | 立案日期 |
| 17 | fcourtregcaseno | 案号 | varchar | 50 |  | √ | ' ' | 案号 |
| 18 | fcourtregjudge | 承办法官 | varchar | 200 |  | √ | ' ' | 承办法官 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pbd_smoni_courtre_fid_fseq |  | fid,fseq |
| 2 | pk_pbd_smoni_courtreentity |  | fentryid |

---

## 外部数据监控库-反写记录表 t_pbd_smoni_data_wb

- **表名称：** 外部数据监控库-反写记录表
- **表名：** t_pbd_smoni_data_wb

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
| 1 | pk_pbd_smoni_data_wb |  | fentryid |
| 2 | idx_pbd_smoni_data_wb_fk |  | fid |

---

## 行政处罚【其它来源】-子表 t_pbd_smoni_opunishentity

- **表名称：** 行政处罚【其它来源】-子表
- **表名：** t_pbd_smoni_opunishentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftypesecond | 处罚类别2 | varchar | 100 |  | √ | ' ' | 处罚类别2 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fevidence | 处罚依据 | varchar | 1000 |  | √ | ' ' | 处罚依据 |
| 5 | freason | 处罚事由 | varchar | 255 |  | √ | ' ' | 处罚事由 |
| 6 | fpublishoid | 合作方Id | int8 | 64 |  | √ | 0 | 合作方Id |
| 7 | freason_tag | 处罚事由_详情 | text | 0 |  |  | null | 处罚事由_详情 |
| 8 | ftype | 处罚类别 | varchar | 100 |  | √ | ' ' | 处罚类别 |
| 9 | fcontent_tag | 处罚结果/内容_详情 | text | 0 |  |  | null | 处罚结果/内容_详情 |
| 10 | fupdatetime | 更新日期 | timestamp | 0 |  |  | null | 更新日期 |
| 11 | fdecisiondate | 决定日期 | timestamp | 0 |  |  | null | 决定日期 |
| 12 | fdepartmentname | 决定机关 | varchar | 512 |  | √ | ' ' | 决定机关 |
| 13 | fcontent | 处罚结果/内容 | varchar | 255 |  | √ | ' ' | 处罚结果/内容 |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 15 | fpunishnumber | 决定文书号 | varchar | 500 |  | √ | ' ' | 决定文书号 |
| 16 | fareaname | 区域 | varchar | 255 |  | √ | ' ' | 区域 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pbd_smoni_opunishentity |  | fentryid |
| 2 | idx_pbd_smoni_opunish_fid_fseq |  | fid,fseq |

---

## 被执行人-子表 t_pbd_smoni_exeentity

- **表名称：** 被执行人-子表
- **表名：** t_pbd_smoni_exeentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fexeccaseno | 案号 | varchar | 50 |  | √ | ' ' | 案号 |
| 3 | fexecmoney | 执行标的 | varchar | 50 |  | √ | ' ' | 执行标的 |
| 4 | fexecpname | 被执行人 | varchar | 255 |  | √ | ' ' | 被执行人 |
| 5 | fexeccasetime | 立案日期 | timestamp | 0 |  |  | null | 立案日期 |
| 6 | fupdatetime | 更新日期 | timestamp | 0 |  |  | null | 更新日期 |
| 7 | fexeccourt | 执行法院 | varchar | 200 |  | √ | ' ' | 执行法院 |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fexecid | 合作方Id | int8 | 64 |  | √ | 0 | 合作方Id |
| 11 | fexecpartycardnum | 组织机构代码 | varchar | 255 |  | √ | ' ' | 组织机构代码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pbd_smoni_exeentity |  | fentryid |
| 2 | idx_pbd_smoni_exe_fid_fseq |  | fid,fseq |

---

## 股权变更-子表 t_pbd_smoni_holderentity

- **表名称：** 股权变更-子表
- **表名：** t_pbd_smoni_holderentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcapital | 现认缴出资额 | varchar | 50 |  | √ | ' ' | 现认缴出资额 |
| 3 | fholderid | 合作方ID | int8 | 64 |  | √ | 0 | 合作方ID |
| 4 | fupdatetime | 更新日期 | timestamp | 0 |  |  | null | 更新日期 |
| 5 | fcapitalbefore | 原认缴出资额 | varchar | 50 |  | √ | ' ' | 原认缴出资额 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fpercentbefore | 原出资比例 | varchar | 50 |  | √ | ' ' | 原出资比例 |
| 9 | fholdername | 股东 | varchar | 255 |  | √ | ' ' | 股东 |
| 10 | fpercent | 现出资比例 | varchar | 50 |  | √ | ' ' | 现出资比例 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pbd_smoni_holderentity |  | fentryid |
| 2 | idx_pbd_smoni_holder_fid_fseq |  | fid,fseq |

---

## 法院公告-子表 t_pbd_smoni_courtanentity

- **表名称：** 法院公告-子表
- **表名：** t_pbd_smoni_courtanentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbltnstate | 公告状态号 | varchar | 50 |  | √ | ' ' | 公告状态号 |
| 3 | fbltndealgrade | 处理等级 | varchar | 255 |  | √ | ' ' | 处理等级 |
| 4 | fbltnjudge | 法官 | varchar | 255 |  | √ | ' ' | 法官 |
| 5 | fbltncontent | 案件内容 | varchar | 2000 |  | √ | ' ' | 案件内容 |
| 6 | fbltndealgradename | 处理等级名称 | varchar | 255 |  | √ | ' ' | 处理等级名称 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fbltntype | 公告类型 | varchar | 50 |  | √ | ' ' | 公告类型 |
| 9 | fbltntypename | 公告类型名称 | varchar | 255 |  | √ | ' ' | 公告类型名称 |
| 10 | fparty2 | 公告人 | varchar | 2000 |  | √ | ' ' | 公告人 |
| 11 | fbltnno | 公告号 | varchar | 50 |  | √ | ' ' | 公告号 |
| 12 | fbltnpublishdate | 刊登日期 | timestamp | 0 |  |  | null | 刊登日期 |
| 13 | fcourtannoid | 合作方Id | int8 | 64 |  | √ | 0 | 合作方Id |
| 14 | fbltncaseno | 案号 | varchar | 200 |  | √ | ' ' | 案号 |
| 15 | fupdatetime | 更新日期 | timestamp | 0 |  |  | null | 更新日期 |
| 16 | fparty1 | 原告 | varchar | 2000 |  | √ | ' ' | 原告 |
| 17 | fbltnpublishpage | 刊登版面 | varchar | 255 |  | √ | ' ' | 刊登版面 |
| 18 | fbltnreason | 原因 | varchar | 500 |  | √ | ' ' | 原因 |
| 19 | fannounceid | 公告id | int8 | 64 |  | √ | 0 | 公告id |
| 20 | fbltncourtcode | 法院名 | varchar | 255 |  | √ | ' ' | 法院名 |
| 21 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 22 | fbltnprovince | 省份 | varchar | 255 |  | √ | ' ' | 省份 |
| 23 | fbltncontent_tag | 案件内容_详情 | text | 0 |  |  | null | 案件内容_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pbd_smoni_courtan_fid_fseq |  | fid,fseq |
| 2 | pk_pbd_smoni_courtanentity |  | fentryid |
