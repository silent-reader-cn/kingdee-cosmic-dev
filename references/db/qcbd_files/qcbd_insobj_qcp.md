# 检验对象(来料)-qcbd_insobj_qcp

## 检验对象(来料)-多语言表 t_qcbd_insobj_qcp_l

- **表名称：** 检验对象(来料)-多语言表
- **表名：** t_qcbd_insobj_qcp_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 检验对象名称 | varchar | 50 |  | √ | ' ' | 检验对象名称 |
| 3 | flocaleid | flocaleid | varchar | 255 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 255 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_qcbd_isolqcp_fname |  | fname |
| 2 | idx_qcbd_isolqcp_fid |  | fid,flocaleid |
| 3 | pk_qcbd_insobj_qcp_l |  | fpkid |

---

## 检验对象(来料)-主表 t_qcbd_insobj_qcp

- **表名称：** 检验对象(来料)-主表
- **表名：** t_qcbd_insobj_qcp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbatchretmsg | 批返内容 | varchar | 255 |  | √ | ' ' | 批返内容 |
| 3 | fsrcentryid | 来源单据分录ID | varchar | 50 |  | √ | ' ' | 来源单据分录ID |
| 4 | fsecondck | fsecondck | bpchar | 1 |  | √ | '0' |  |
| 5 | fsrcbillno | 来源单据编号 | varchar | 500 |  | √ | ' ' | 来源单据编号 |
| 6 | fsumunqualifbaseqty | 不合格数(基本) | numeric | 23 | 10 | √ | 0 | 不合格数(基本) |
| 7 | fsbillno | 生成单据编号 | varchar | 50 |  | √ | ' ' | 生成单据编号 |
| 8 | fsrcentryseq | 来源分录实体序号 | int8 | 64 |  | √ | 0 | 来源分录实体序号 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fsrcbaseqty | 来源数量（基本） | numeric | 23 | 10 | √ | 0 | 来源数量（基本） |
| 11 | fstatus | 数据状态 | varchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fsrcmaterialid | 来源物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 15 | fbatchretmsg_tag | 批返内容_详情 | text | 0 |  |  | '' | 批返内容_详情 |
| 16 | fsrcqty | 来源数量 | numeric | 23 | 10 | √ | 0 | 来源数量 |
| 17 | fsbillentryid | 生成单据分录ID | varchar | 50 |  | √ | ' ' | 生成单据分录ID |
| 18 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 19 | fsrcbaseunitid | 来源计量单位(基本) | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 20 | fsumqualifbaseqty | 合格数(基本) | numeric | 23 | 10 | √ | 0 | 合格数(基本) |
| 21 | fbatchretflg | 批返标记 | bpchar | 1 |  | √ | '0' | 批返标记 |
| 22 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 23 | fname | 检验对象名称 | varchar | 50 |  | √ | ' ' | 检验对象名称 |
| 24 | fsentitynumberid | 生成单据主实体对象 | varchar | 255 |  | √ | '0' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 25 | fbatchno | fbatchno | int8 | 64 |  | √ | 0 |  |
| 26 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 27 | fsrcbillid | 来源单据ID | varchar | 50 |  | √ | ' ' | 来源单据ID |
| 28 | fsrcunitid | 来源计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 29 | fsrcentitynumber | 来源单据实体 | varchar | 50 |  | √ | ' ' | 来源单据实体 |
| 30 | fsumsrcqualifqty | 合格数(来源单位) | numeric | 23 | 10 | √ | 0 | 合格数(来源单位) |
| 31 | fscsystem | 来源系统 | varchar | 50 |  | √ | ' ' | 来源系统 |
| 32 | fsbillid | 生成单据ID | varchar | 50 |  | √ | ' ' | 生成单据ID |
| 33 | fsumsrcunqualifqty | 不合格数(来源单位) | numeric | 23 | 10 | √ | 0 | 不合格数(来源单位) |
| 34 | fenable | 使用状态 | varchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 35 | fnumber | 检验对象编码 | varchar | 30 |  | √ | ' ' | 检验对象编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_qcbd_insobj_qcp |  | fid |
| 2 | idx_qcbd_isoqcp_fcreatetime |  | fcreatetime |
| 3 | idx_qcbd_isoqcp_fnumber |  | fnumber |

---

## 单据体-子表 t_qcbd_qcpo_entry

- **表名称：** 单据体-子表
- **表名：** t_qcbd_qcpo_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsecondck | 二次检验 | bpchar | 1 |  | √ | '0' | 二次检验 |
| 3 | fqualifsrcqty | 合格数(来源单位) | numeric | 23 | 10 | √ | 0 | 合格数(来源单位) |
| 4 | fqualifqty | 合格数 | numeric | 23 | 10 | √ | 0 | 合格数 |
| 5 | finspfirstentrykey | 首次检验分录唯一标识 | varchar | 50 |  | √ | ' ' | 首次检验分录唯一标识 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fbillentryseq | 关联单据分录序号 | int4 | 32 |  | √ | 0 | 关联单据分录序号 |
| 8 | fqualifbaseqty | 合格数(基本) | numeric | 23 | 10 | √ | 0 | 合格数(基本) |
| 9 | funqualifqty | 不合格数 | numeric | 23 | 10 | √ | 0 | 不合格数 |
| 10 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :提交 C :审核 |
| 11 | fentrynumber | 关联单据分录标识 | varchar | 20 |  | √ | ' ' | 关联单据分录标识 |
| 12 | fupdtime | 更新时间 | timestamp | 0 |  |  | null | 更新时间 |
| 13 | fentitynumberid | 关联单据实体 | varchar | 255 |  | √ | '0' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 14 | fhandmethed | 处理方式（旧） | varchar | 9 |  | √ | ' ' | 处理方式（旧）,枚举: qcpA :退货 qcpB :报废 qcpC :让步接收 qcpT :挑选 qcppA :返工 qcppB :报废 qcppC :让步接收 qcppT :挑选 qcppE :返修 qcppG :工废 qcppL :料废 qcasB :报废 qcasC :让步接收 qcasF :让步放行 qcasT :挑选 qcnpB :报废 qcnpT :挑选 |
| 15 | finspresbillid | 检验结果内码 | int8 | 64 |  | √ | 0 | 检验结果内码 |
| 16 | fbillno | 关联单据编号 | varchar | 50 |  | √ | ' ' | 关联单据编号 |
| 17 | fbaddealinfoentryseq | 不良处理信息分录号 | int8 | 64 |  | √ | 0 | 不良处理信息分录号 |
| 18 | funitid | 关联计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 19 | funqualifbaseqty | 不合格数(基本) | numeric | 23 | 10 | √ | 0 | 不合格数(基本) |
| 20 | fassnewhandid | 处理方式 | int8 | 64 |  | √ | 0 | [不良品处理方式 bd_badhandmode](../basedata_files/bd_badhandmode.md) |
| 21 | fbaddealinfoentryid | 不良处理信息分录ID | varchar | 50 |  | √ | ' ' | 不良处理信息分录ID |
| 22 | fbillentryid | 关联单据分录ID | varchar | 50 |  | √ | ' ' | 关联单据分录ID |
| 23 | fcusttextval | 自定义文本值 | varchar | 2000 |  | √ | ' ' | 自定义文本值 |
| 24 | fbillid | 关联单据ID | varchar | 50 |  | √ | ' ' | 关联单据ID |
| 25 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 26 | funqualifsrcqty | 不合格数(来源单位) | numeric | 23 | 10 | √ | 0 | 不合格数(来源单位) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_qcbd_isoqcp_fbillid |  | fentitynumberid,fbillid |
| 2 | idx_qcbd_isoqcp_fid |  | fid |
| 3 | pk_qcbd_qcpo_entry |  | fentryid |
| 4 | idx_qcbd_isoqcp_fseq |  | fseq |
