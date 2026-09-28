# 生成内部交易单据记录-ism_settlelog

## 生成内部交易单据记录-主表 t_ism_settlelog

- **表名称：** 生成内部交易单据记录-主表
- **表名：** t_ism_settlelog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsourcenum | 来源单据编号 | varchar | 80 |  | √ | ' ' | 来源单据编号 |
| 3 | fbillstatus | fbillstatus | bpchar | 1 |  | √ | 'A' |  |
| 4 | fcreatestatus | 生成单据状态 | bpchar | 1 |  | √ | 'C' | 生成单据状态,枚举: A :全部审核成功 E :全部保存成功 N :无需生成内部交易单据 B :部分保存成功 W :结算执行中 C :全部执行失败 D :内部交易单据已删除 U :路径匹配失败 G :等待生成内部交易单据 |
| 5 | foppositeorg | foppositeorg | int8 | 64 |  | √ | 0 |  |
| 6 | fsourceid | 来源单据id | int8 | 64 |  | √ | 0 | 来源单据id |
| 7 | fbiztraceno | 业务跟踪号 | varchar | 50 |  | √ | ' ' | 业务跟踪号 |
| 8 | fshouldcount | 应生成结算单数量 | int8 | 64 |  | √ | 0 | 应生成结算单数量 |
| 9 | factualcount | 实际生成结算单数量 | int8 | 64 |  | √ | 0 | 实际生成结算单数量 |
| 10 | fretrycount | 重试次数 | int4 | 32 |  | √ | 0 | 重试次数 |
| 11 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 12 | fbillfailcause | 生成单据失败原因 | varchar | 255 |  | √ | ' ' | 生成单据失败原因 |
| 13 | fsupsettleorg | fsupsettleorg | int8 | 64 |  | √ | 0 |  |
| 14 | fsourcetype | 来源单据对象 | varchar | 80 |  | √ | ' ' | [单据主实体 bos_billmainentity](../mdl_files/bos_billmainentity.md) |
| 15 | feditdate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 16 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ism_slog_fsid |  | fsourceid |
| 2 | t_ism_settlelog_pkey |  | fid |
| 3 | idx_ism_slog_fsno |  | fsourcenum |

---

## 单据体-子表 t_ism_settlelog_detail

- **表名称：** 单据体-子表
- **表名：** t_ism_settlelog_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbotpid | 转换规则 | varchar | 40 |  | √ | ' ' | [转换规则 botp_crlist](../botp_files/botp_crlist.md) |
| 3 | frelationtype | 结算单据类型 | varchar | 50 |  | √ | ' ' | 结算单据类型,枚举: supplier :供应方 demand :需求方 toouter :对外 other :其他 |
| 4 | fedemandorgid | 当前段需求方结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fgroupnumber | 成组号 | varchar | 100 |  | √ | ' ' | 成组号 |
| 7 | fsettlepath | 结算路径分录段 | int8 | 64 |  | √ | 0 | 结算路径分录段 |
| 8 | fgroupkey | 分组标识 | varchar | 100 |  | √ | ' ' | 分组标识 |
| 9 | ffailcause | 失败原因 | varchar | 2000 |  | √ | ' ' | 失败原因 |
| 10 | fopertype | 上一次操作类型 | varchar | 50 |  | √ | ' ' | 上一次操作类型,枚举: settle :生成 unsettle :取消生成 |
| 11 | fsettlebillid | 结算单id | int8 | 64 |  | √ | 0 | 结算单id |
| 12 | fsettledate | 生成日期 | timestamp | 0 |  |  | null | 生成日期 |
| 13 | fsettlebilltypenum | 内部交易单据对象 | varchar | 80 |  | √ | ' ' | [单据主实体 bos_billmainentity](../mdl_files/bos_billmainentity.md) |
| 14 | fsettlebilltypeid | fsettlebilltypeid | int8 | 64 |  | √ | 0 |  |
| 15 | fbillcreatestatus | 单据生成状态 | varchar | 50 |  | √ | ' ' | 单据生成状态,枚举: 9 :结算路径不一致 0 :未生成 6 :未指定结算路径 7 :路径匹配失败 2 :已生成 1 :未保存 |
| 16 | fsettlerelation | 结算路径 | int8 | 64 |  | √ | 0 | [结算路径 ism_settlerelations](../ism_files/ism_settlerelations.md) |
| 17 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: 0 :未生成 1 :未保存 2 :暂存 3 :提交 4 :审核 5 :已删除 6 :未指定结算路径 7 :路径匹配失败 N :无需生成内部交易单据 |
| 18 | foppositeorg | 需求方业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 19 | fiswriteoff | 是否已核销 | bpchar | 1 |  | √ | '0' | 是否已核销 |
| 20 | fiscreat | 是否生成成功 | bpchar | 1 |  | √ | '0' | 是否生成成功 |
| 21 | fesupsettleorgid | 当前段供应方结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 22 | fsupsettleorg | 供应方业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 23 | fbizflow | 业务流程 | int8 | 64 |  | √ | 0 | [流程设计 wf_model](../wf_files/wf_model.md) |
| 24 | fsettlebillno | 内部交易单据编号 | varchar | 50 |  | √ | ' ' | 内部交易单据编号 |
| 25 | fiscreatpayment | 是否生成应收应付 | bpchar | 1 |  | √ | '0' | 是否生成应收应付 |
| 26 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 27 | fsettlepathtext | 结算路径段 | varchar | 255 |  | √ | ' ' | 结算路径段 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_ism_slogd_fsbid |  | fsettlebillid |
| 2 | t_ism_settlelog_detail_pkey |  | fentryid |
| 3 | idx_ism_stlog_fid |  | fid |
