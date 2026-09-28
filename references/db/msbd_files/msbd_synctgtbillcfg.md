# 同步下游单据配置-msbd_synctgtbillcfg

## 同步下游单据配置-多语言表 t_msbd_synctgtbillcfg_l

- **表名称：** 同步下游单据配置-多语言表
- **表名：** t_msbd_synctgtbillcfg_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 512 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msbd_synctgtbillcfg_l_0 |  | fid,flocaleid |
| 2 | pk_msbd_synctgtbillcfg_l |  | fpkid |

---

## 下游单据-子表 t_msbd_synctgtbillmap

- **表名称：** 下游单据-子表
- **表名：** t_msbd_synctgtbillmap

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftprecondition_tag | 前置条件_详情 | text | 0 |  |  | null | 前置条件_详情 |
| 3 | ftprecondition | 前置条件 | varchar | 255 |  | √ | ' ' | 前置条件 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | ftgtfilter | 过滤服务 | varchar | 2000 |  | √ | ' ' | 过滤服务,枚举: kd.mpscmm.msbd.syncbill.ext.VoucherFilter :排除已生成凭证的单据 |
| 6 | fsaveopt | 保存操作参数 | varchar | 2000 |  | √ | ' ' | 保存操作参数 |
| 7 | ftargetentitymapid | 来源字段配置 | int8 | 64 |  | √ | 0 | [通用映射配置 sbs_billfieldmapping](../mscommon_files/sbs_billfieldmapping.md) |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msbd_synctgtbillmap_fk |  | fid |
| 2 | pk_msbd_synctgtbillmap |  | fentryid |

---

## 同步下游单据配置-主表 t_msbd_synctgtbillcfg

- **表名称：** 同步下游单据配置-主表
- **表名：** t_msbd_synctgtbillcfg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | fsprecondition | 源单前置条件 | varchar | 255 |  | √ | ' ' | 源单前置条件 |
| 5 | fresultfieldmapid | 结果字段配置 | int8 | 64 |  | √ | 0 | [通用映射配置 sbs_billfieldmapping](../mscommon_files/sbs_billfieldmapping.md) |
| 6 | fsprecondition_tag | 源单前置条件_详情 | text | 0 |  |  | null | 源单前置条件_详情 |
| 7 | flistentityid | 列表单据 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 8 | fshownochange | 展示无变更分录 | bpchar | 1 |  | √ | '0' | 展示无变更分录 |
| 9 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 10 | fsrcentitymapid | 源单来源字段配置 | int8 | 64 |  | √ | 0 | [通用映射配置 sbs_billfieldmapping](../mscommon_files/sbs_billfieldmapping.md) |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fpreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 16 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 17 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 18 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | flistbillhdlsvc | 列表单据处理服务 | varchar | 2000 |  | √ | ' ' | 列表单据处理服务,枚举: kd.mpscmm.msbd.syncbill.ext.PriceConvSvc :单位价格换算 kd.mpscmm.msbd.syncbill.ext.SyncPriceDataSvc :同步价格数据服务 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msbd_synctgtbillcfg_number |  | fnumber |
| 2 | pk_msbd_synctgtbillcfg |  | fid |

---

## 可同步字段-子表 t_msbd_syncfield

- **表名称：** 可同步字段-子表
- **表名：** t_msbd_syncfield

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsyncfield | 同步字段标识 | varchar | 255 |  | √ | ' ' | 同步字段标识 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msbd_syncfield_fk |  | fid |
| 2 | pk_msbd_syncfield |  | fentryid |

---

## 下游存在单据禁止同步-子表 t_msbd_excludetgtbill

- **表名称：** 下游存在单据禁止同步-子表
- **表名：** t_msbd_excludetgtbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fexcludefilter | 过滤服务 | varchar | 2000 |  | √ | ' ' | 过滤服务,枚举: kd.mpscmm.msbd.syncbill.ext.VoucherFilter :已生成凭证 kd.mpscmm.msbd.syncbill.ext.InvCloseDateFilter :已关账的库存单据 kd.mpscmm.msbd.syncbill.ext.FinCloseDataFilter :已关账的财务单据 |
| 3 | fexcludetgtid | 下游单据 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 4 | feprecondition | 前置条件 | varchar | 255 |  | √ | ' ' | 前置条件 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | feprecondition_tag | 前置条件_详情 | text | 0 |  |  | null | 前置条件_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_msbd_excludetgtbill |  | fentryid |
| 2 | idx_msbd_excludetgtbill_fk |  | fid |
