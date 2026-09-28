# 来料检验结果-qcp_inspresult

## 来料检验结果-主表 t_qcp_inspresult

- **表名称：** 来料检验结果-主表
- **表名：** t_qcp_inspresult

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fckdamageqtybasic | 样本破坏数（基本） | numeric | 23 | 10 | √ | 0 | 样本破坏数（基本） |
| 3 | fassbillid | 生成单据ID | varchar | 50 |  | √ | ' ' | 生成单据ID |
| 4 | fckqualifbaseqty | 汇总检验合格数(基本) | numeric | 23 | 10 | √ | 0 | 汇总检验合格数(基本) |
| 5 | fckdamagebear | 样本破坏承担方 | bpchar | 1 |  | √ | ' ' | 样本破坏承担方,枚举: A :供应商 B :我方 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fckhandmethed | 不良处理方式（旧） | varchar | 10 |  | √ | ' ' | 不良处理方式（旧）,枚举: qcpA :退货 qcpB :报废 qcpC :让步接收 qcpT :挑选 |
| 8 | fassbillentryseq | 生成单据分录序号 | int8 | 64 |  | √ | 0 | 生成单据分录序号 |
| 9 | fckbaseunitid | 检验计量单位(基本) | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fckunitid | 检验计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 12 | fassbillno | 生成单据编号 | varchar | 50 |  | √ | ' ' | 生成单据编号 |
| 13 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 14 | fckdiscountcurrency | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 15 | fckmaterialid | 检验物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 16 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 17 | finsobjid | 检验对象内码 | int8 | 64 |  | √ | 0 | 检验对象内码 |
| 18 | fassbillentryid | 生成单据分录ID | varchar | 50 |  | √ | ' ' | 生成单据分录ID |
| 19 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fbillstatus | 单据状态 | varchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 21 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 22 | finsobjentryid | 检验对象分录内码 | int8 | 64 |  | √ | 0 | 检验对象分录内码 |
| 23 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 24 | fcknewhandid | 不良品处理方式 | int8 | 64 |  | √ | 0 | [不良品处理方式 bd_badhandmode](../basedata_files/bd_badhandmode.md) |
| 25 | fckunqualifbaseqty | 汇总检验不合格数(基本) | numeric | 23 | 10 | √ | 0 | 汇总检验不合格数(基本) |
| 26 | fexecstatus | 执行状态 | varchar | 10 |  | √ | ' ' | 执行状态,枚举: created :已创建 completed :已完成 executing :正在处理 received :已经接收准备处理 errored :异常 |
| 27 | fckqualifqty | 汇总检验合格数 | numeric | 23 | 10 | √ | 0 | 汇总检验合格数 |
| 28 | fckdamageqty | 样本破坏数 | numeric | 23 | 10 | √ | 0 | 样本破坏数 |
| 29 | fckauxpty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 30 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 31 | fckunqualifqty | 汇总检验不合格数 | numeric | 23 | 10 | √ | 0 | 汇总检验不合格数 |
| 32 | fassentitynumberid | 生成单据实体 | varchar | 255 |  | √ | '0' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 33 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 34 | fckdiscountamount | 折让金额 | numeric | 23 | 10 | √ | 0 | 折让金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_qcp_insplt_fcreatetime |  | fcreatetime |
| 2 | idx_qcp_insplt_fbillno |  | fbillno |
| 3 | idx_qcp_inspresult_assbill |  | fassentitynumberid,fassbillid |
| 4 | pk_qcp_inspresult |  | fid |

---

## 关联子实体-子表 t_qcp_resultentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_qcp_resultentry_lk

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
| 1 | idx_qcp_resultentry_lk_fk |  | fentryid |
| 2 | pk_qcp_resultentry_lk |  | fpkid |

---

## 来料检验结果-关联追踪表 t_qcp_inspresult_tc

- **表名称：** 来料检验结果-关联追踪表
- **表名：** t_qcp_inspresult_tc

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
| 1 | idx_qcp_inspresult_tc_tbill |  | ftbillid |
| 2 | pk_qcp_inspresult_tc |  | fid |
| 3 | idx_qcp_inspresult_tc_tid |  | ftid |

---

## 关联子实体-子表 t_qcp_inspresult_lk

- **表名称：** 关联子实体-子表
- **表名：** t_qcp_inspresult_lk

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
| 1 | idx_qcp_inspresult_lk_fk |  | fid |
| 2 | pk_qcp_inspresult_lk |  | fpkid |

---

## 来料检验结果-反写记录表 t_qcp_inspresult_wb

- **表名称：** 来料检验结果-反写记录表
- **表名：** t_qcp_inspresult_wb

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
| 1 | pk_qcp_inspresult_wb |  | fentryid |
| 2 | idx_qcp_inspresult_wb_fk |  | fid |

---

## 分批信息-单据体-子表 t_qcp_resultentry

- **表名称：** 分批信息-单据体-子表
- **表名：** t_qcp_resultentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fqualifybaseqty | 检验合格数(基本) | numeric | 23 | 10 | √ | 0 | 检验合格数(基本) |
| 3 | fsrcsystem | 送检单据来源系统 | varchar | 50 |  | √ | ' ' | 送检单据来源系统,枚举: |
| 4 | fsubmitunitid | 送检单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 5 | fsrcentitynumberid | 送检来源单据实体 | varchar | 50 |  | √ | '0' | 送检来源单据实体 |
| 6 | fsrcbillno | 送检来源单据编号 | varchar | 500 |  | √ | ' ' | 送检来源单据编号 |
| 7 | fqualifqty | 检验合格数 | numeric | 23 | 10 | √ | 0 | 检验合格数 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fsamplingresult | 质量判定 | varchar | 5 |  | √ | ' ' | 质量判定,枚举: B :接受 C :不接受 |
| 10 | furgentrelease | 紧急放行 | bpchar | 1 |  | √ | '0' | 紧急放行 |
| 11 | fsrcbillentryseq | 送检来源单据分录序号 | int8 | 64 |  | √ | 0 | 送检来源单据分录序号 |
| 12 | funqualifqty | 检验不合格数 | numeric | 23 | 10 | √ | 0 | 检验不合格数 |
| 13 | fassignqty | fassignqty | numeric | 23 | 10 | √ | 0 |  |
| 14 | fsrcbillsplitentryid | 送检来源单据拆分分录ID | int8 | 64 |  | √ | 0 | 送检来源单据拆分分录ID |
| 15 | fdsrcbillid | 检验单单据ID | varchar | 50 |  | √ | ' ' | 检验单单据ID |
| 16 | fdsrcbillentryseq | 检验单来源信息分录序号 | int8 | 64 |  | √ | 0 | 检验单来源信息分录序号 |
| 17 | fbaddealinfoentryseq | 不良处理信息分录号 | int8 | 64 |  | √ | 0 | 不良处理信息分录号 |
| 18 | fsrcbillid | 送检来源单据ID | varchar | 50 |  | √ | ' ' | 送检来源单据ID |
| 19 | funqualifbaseqty | 检验不合格数(基本) | numeric | 23 | 10 | √ | 0 | 检验不合格数(基本) |
| 20 | fdsrcentitynumberid | 检验单实体 | varchar | 255 |  | √ | '0' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 21 | fdsrcentrynumber | 检验单分录标识 | varchar | 20 |  | √ | ' ' | 检验单分录标识 |
| 22 | fdsrcbillentryid | 检验单来源信息分录ID | varchar | 50 |  | √ | ' ' | 检验单来源信息分录ID |
| 23 | fsrcbillentryid | 送检来源单据分录ID | varchar | 50 |  | √ | ' ' | 送检来源单据分录ID |
| 24 | fbaddealinfoentryid | 不良处理信息分录ID | varchar | 50 |  | √ | ' ' | 不良处理信息分录ID |
| 25 | fassignbaseqty | fassignbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 26 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_qcp_resultentry |  | fentryid |
| 2 | idx_qcp_resury_fseq |  | fseq |
| 3 | idx_qcp_resury_fid |  | fid |
