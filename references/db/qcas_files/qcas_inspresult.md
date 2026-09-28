# 销售检验结果-qcas_inspresult

## 关联子实体-子表 t_qcas_inspresult_lk

- **表名称：** 关联子实体-子表
- **表名：** t_qcas_inspresult_lk

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
| 1 | idx_qcas_inspresult_lk_fk |  | fid |
| 2 | pk_qcas_inspresult_lk |  | fpkid |

---

## 关联子实体-子表 t_qcas_resultentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_qcas_resultentry_lk

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
| 1 | idx_qcas_resultentry_lk_fk |  | fentryid |
| 2 | pk_qcas_resultentry_lk |  | fpkid |

---

## 销售检验结果-主表 t_qcas_inspresult

- **表名称：** 销售检验结果-主表
- **表名：** t_qcas_inspresult

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fassbillid | 生成单据ID | varchar | 50 |  | √ | ' ' | 生成单据ID |
| 3 | fckqualifbaseqty | 汇总检验合格数(基本) | numeric | 23 | 10 | √ | 0 | 汇总检验合格数(基本) |
| 4 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 5 | fckhandmethed | 不良处理方式（旧） | varchar | 10 |  | √ | ' ' | 不良处理方式（旧）,枚举: qcasB :报废 qcasC :让步接收 qcasF :让步放行 qcasT :挑选 |
| 6 | fassbillentryseq | 生成单据分录序号 | int8 | 64 |  | √ | 0 | 生成单据分录序号 |
| 7 | fckbaseunitid | 检验计量单位(基本) | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fckunitid | 检验计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 10 | fassbillno | 生成单据编号 | varchar | 50 |  | √ | ' ' | 生成单据编号 |
| 11 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 12 | fckmaterialid | 检验物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 13 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 14 | finsobjid | 检验对象内码 | int8 | 64 |  | √ | 0 | 检验对象内码 |
| 15 | fsalesreturn | 是否退货 | varchar | 1 |  | √ | '0' | 是否退货 |
| 16 | fassbillentryid | 生成单据分录ID | varchar | 50 |  | √ | ' ' | 生成单据分录ID |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | fqualirefund | 合格品退货 | varchar | 1 |  | √ | '0' | 合格品退货 |
| 19 | fbillstatus | 单据状态 | varchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | finsobjentryid | 检验对象分录内码 | int8 | 64 |  | √ | 0 | 检验对象分录内码 |
| 22 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 23 | fcknewhandid | 不良品处理方式 | int8 | 64 |  | √ | 0 | 不良品处理方式 bd_badhandmode |
| 24 | fckunqualifbaseqty | 汇总检验不合格数(基本) | numeric | 23 | 10 | √ | 0 | 汇总检验不合格数(基本) |
| 25 | fexecstatus | 执行状态 | varchar | 10 |  | √ | ' ' | 执行状态,枚举: created :已创建 completed :已完成 executing :正在处理 received :已经接收准备处理 errored :异常 |
| 26 | fckqualifqty | 汇总检验合格数 | numeric | 23 | 10 | √ | 0 | 汇总检验合格数 |
| 27 | fdisqualsales | 不合格可销售 | varchar | 1 |  | √ | '0' | 不合格可销售 |
| 28 | fckauxpty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 29 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 30 | fckunqualifqty | 汇总检验不合格数 | numeric | 23 | 10 | √ | 0 | 汇总检验不合格数 |
| 31 | fassentitynumberid | 生成单据实体 | varchar | 255 |  | √ | '0' | 主实体对象 bos_entityobject |
| 32 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_qcas_insplt_fcreatetime |  | fcreatetime |
| 2 | idx_qcas_inspresult_assbill |  | fassentitynumberid,fassbillid |
| 3 | idx_qcas_insplt_fbillno |  | fbillno |
| 4 | pk_qcas_inspresult |  | fid |

---

## 销售检验结果-反写记录表 t_qcas_inspresult_wb

- **表名称：** 销售检验结果-反写记录表
- **表名：** t_qcas_inspresult_wb

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
| 1 | idx_qcas_inspresult_wb_fk |  | fid |
| 2 | pk_qcas_inspresult_wb |  | fentryid |

---

## 分批信息-单据体-子表 t_qcas_resultentry

- **表名称：** 分批信息-单据体-子表
- **表名：** t_qcas_resultentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fqualifybaseqty | 检验合格数(基本) | numeric | 23 | 10 | √ | 0 | 检验合格数(基本) |
| 3 | fsrcsystem | 送检单据来源系统 | varchar | 50 |  | √ | ' ' | 送检单据来源系统,枚举: |
| 4 | fsubmitunitid | 送检单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 5 | fsrcentitynumberid | 送检来源单据实体 | varchar | 50 |  | √ | '0' | 送检来源单据实体 |
| 6 | fsrcbillno | 送检来源单据编号 | varchar | 500 |  | √ | ' ' | 送检来源单据编号 |
| 7 | fqualifqty | 检验合格数 | numeric | 23 | 10 | √ | 0 | 检验合格数 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fsamplingresult | 质量判定 | varchar | 5 |  | √ | ' ' | 质量判定,枚举: B :接受 C :不接受 |
| 10 | fsrcbillentryseq | 送检来源单据分录序号 | int8 | 64 |  | √ | 0 | 送检来源单据分录序号 |
| 11 | funqualifqty | 检验不合格数 | numeric | 23 | 10 | √ | 0 | 检验不合格数 |
| 12 | fassignqty | fassignqty | numeric | 23 | 10 | √ | 0 |  |
| 13 | fsrcbillsplitentryid | 送检来源单据拆分分录ID | int8 | 64 |  | √ | 0 | 送检来源单据拆分分录ID |
| 14 | fdsrcbillid | 检验单单据ID | varchar | 50 |  | √ | ' ' | 检验单单据ID |
| 15 | fdsrcbillentryseq | 检验单来源信息分录序号 | int8 | 64 |  | √ | 0 | 检验单来源信息分录序号 |
| 16 | fbaddealinfoentryseq | 不良处理信息分录号 | int8 | 64 |  | √ | 0 | 不良处理信息分录号 |
| 17 | fsrcbillid | 送检来源单据ID | varchar | 50 |  | √ | ' ' | 送检来源单据ID |
| 18 | funqualifbaseqty | 检验不合格数(基本) | numeric | 23 | 10 | √ | 0 | 检验不合格数(基本) |
| 19 | fdsrcentitynumberid | 检验单实体 | varchar | 255 |  | √ | '0' | 主实体对象 bos_entityobject |
| 20 | fdsrcentrynumber | 检验单分录标识 | varchar | 20 |  | √ | ' ' | 检验单分录标识 |
| 21 | fdsrcbillentryid | 检验单来源信息分录ID | varchar | 50 |  | √ | ' ' | 检验单来源信息分录ID |
| 22 | fsrcbillentryid | 送检来源单据分录ID | varchar | 50 |  | √ | ' ' | 送检来源单据分录ID |
| 23 | fbaddealinfoentryid | 不良处理信息分录ID | varchar | 50 |  | √ | ' ' | 不良处理信息分录ID |
| 24 | fassignbaseqty | fassignbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 25 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_qcas_resultentry_fsrcbillentryid |  | fsrcbillentryid |
| 2 | pk_qcas_resultentry |  | fentryid |
| 3 | idx_qcas_resury_fid |  | fid |
| 4 | idx_qcas_resury_fseq |  | fseq |

---

## 销售检验结果-关联追踪表 t_qcas_inspresult_tc

- **表名称：** 销售检验结果-关联追踪表
- **表名：** t_qcas_inspresult_tc

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
| 1 | idx_qcas_inspresult_tc_tbill |  | ftbillid |
| 2 | pk_qcas_inspresult_tc |  | fid |
| 3 | idx_qcas_inspresult_tc_tid |  | ftid |
