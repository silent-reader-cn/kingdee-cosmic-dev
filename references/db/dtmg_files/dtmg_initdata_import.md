# 快速初始化数据迁移-dtmg_initdata_import

## 快速初始化数据迁移-主表 t_dtmg_initimport

- **表名称：** 快速初始化数据迁移-主表
- **表名：** t_dtmg_initimport

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | 名称 | varchar | 150 |  | √ | ' ' | 名称 |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fimpstatus | 迁移结果 | varchar | 50 |  | √ | ' ' | 迁移结果,枚举: A :暂存 B :执行中 P :部分成功 C :导入成功 D :导入失败 E :已关闭 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fexecutebegindate | 开始执行时间 | timestamp | 0 |  |  | null | 开始执行时间 |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | ftasknum | 迁移对象数量 | int8 | 64 |  | √ | 0 | 迁移对象数量 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fsourcetype | 来源系统 | varchar | 3 |  | √ | ' ' | 来源系统,枚举: 1 :企业版/标准版 2 :K/3 WISE 3 :U8 |
| 13 | fexecuteenddate | 执行结束时间 | timestamp | 0 |  |  | null | 执行结束时间 |
| 14 | fserviceid | 后台导入服务id | varchar | 255 |  | √ | ' ' | 后台导入服务id |
| 15 | fexecutetype | 执行方式 | varchar | 2 |  | √ | '1' | 执行方式,枚举: 1 :手动导入 2 :系统迁移 |
| 16 | fusetime | 用时（秒） | int8 | 64 |  | √ | 0 | 用时（秒） |
| 17 | fbillno | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 18 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_dtmg_initimport |  | fid |
| 2 | idx_dtmg_initimport |  | fbillno |

---

## 快速初始化数据迁移-多语言表 t_dtmg_initimport_l

- **表名称：** 快速初始化数据迁移-多语言表
- **表名：** t_dtmg_initimport_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 150 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_dtmg_initimport_l |  | fid,flocaleid |
| 2 | pk_t_dtmg_initimport_l |  | fpkid |

---

## 初始化导入分录-子表 t_dtmg_initimportentry

- **表名称：** 初始化导入分录-子表
- **表名：** t_dtmg_initimportentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fintegerfield | 整数 | int8 | 64 |  | √ | 0 | 整数 |
| 3 | ffailreason_tag | 失败原因_详情 | text | 0 |  |  | null | 失败原因_详情 |
| 4 | fschemeid | fschemeid | int8 | 64 |  | √ | 0 |  |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fuploadfile | 已上传文件 | varchar | 50 |  | √ | ' ' | 已上传文件 |
| 7 | flogid | 失败日志id | int8 | 64 |  | √ | 0 | 失败日志id |
| 8 | fimportresult | 导入结果 | varchar | 50 |  | √ | ' ' | 导入结果,枚举: A :暂存 B :执行中 C :导入成功 D :导入失败 E :已关闭 P :部分成功 |
| 9 | ftextfield | ftextfield | varchar | 50 |  | √ | ' ' |  |
| 10 | fimplogid | 导入结果日志id | int8 | 64 |  | √ | 0 | 导入结果日志id |
| 11 | ffailcnt | 失败数量 | int8 | 64 |  | √ | 0 | 失败数量 |
| 12 | fbusinessname | 导入业务对象 | varchar | 100 |  | √ | ' ' | 导入业务对象 |
| 13 | ffailreason | 失败原因 | varchar | 1000 |  | √ | ' ' | 失败原因 |
| 14 | fretransmittasktplurl | 重传文件相对地址 | varchar | 512 |  | √ | ' ' | 重传文件相对地址 |
| 15 | fretransmituid | 重传文件标识 | varchar | 50 |  | √ | ' ' | 重传文件标识 |
| 16 | fbillentity | fbillentity | varchar | 50 |  | √ | ' ' |  |
| 17 | fimporttype | 导入方式 | varchar | 50 |  | √ | ' ' | 导入方式,枚举: new :添加新数据 override :更新已有数据 overridenew :更新已有数据并添加新数据 |
| 18 | fcode | 导入顺序 | varchar | 50 |  | √ | ' ' | 导入顺序 |
| 19 | fbusinessnumber | fbusinessnumber | varchar | 50 |  | √ | ' ' |  |
| 20 | fimportpattern | fimportpattern | varchar | 50 |  | √ | ' ' |  |
| 21 | fuidfile | 文件标识 | varchar | 512 |  | √ | ' ' | 文件标识 |
| 22 | freplacekeyfield | 数据替换规则的唯一值 | varchar | 255 |  | √ | ' ' | 数据替换规则的唯一值 |
| 23 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 24 | fdatacount | 数据统计 | varchar | 512 |  | √ | ' ' | 数据统计 |
| 25 | ftasktplurl | 文件相对地址 | varchar | 512 |  | √ | ' ' | 文件相对地址 |
| 26 | fclasstype | 所属分类 | varchar | 50 |  | √ | ' ' | 所属分类,枚举: A :基础资料 B :财务 C :供应链 D :制造 |
| 27 | fmodifydatefield | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 28 | fdatacount_tag | fdatacount_tag | text | 0 |  |  | null |  |
| 29 | fexecstatus | 执行状态 | varchar | 50 |  | √ | ' ' | 执行状态 |
| 30 | fbusinessno | 业务对象标识 | varchar | 50 |  | √ | ' ' | 业务对象标识 |
| 31 | freplacekeyword | 数据替换规则的唯一值 | varchar | 512 |  | √ | ' ' | 数据替换规则的唯一值 |
| 32 | fbillentityid | fbillentityid | int8 | 64 |  | √ | 0 |  |
| 33 | furl | url地址 | varchar | 512 |  | √ | ' ' | url地址 |
| 34 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_dtmg_initimportentry |  | fentryid |
| 2 | idx_dtmg_initimportentry |  | fid |

---

## 重传附件-附件表 t_dtmg_initimportentry_ot

- **表名称：** 重传附件-附件表
- **表名：** t_dtmg_initimportentry_ot

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [附件字段实体 bd_attachment](../frame_files/bd_attachment.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | FPKID |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_dtmg_initimportentry_ot |  | fpkid |
| 2 | idx_tmg_initimportentry_ot |  | fentryid |
