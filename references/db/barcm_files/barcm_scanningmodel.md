# 条码扫描模型-barcm_scanningmodel

## 条码扫描模型-使用范围表 t_barcm_scmodel_u

- **表名称：** 条码扫描模型-使用范围表
- **表名：** t_barcm_scmodel_u

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcreateorgid | fcreateorgid | int8 | 64 |  |  | null |  |
| 2 | fdataid | fdataid | int8 | 64 |  | √ | null |  |
| 3 | fuseorgid | fuseorgid | int8 | 64 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdataid | fdataid,fuseorgid |
| 2 | fuseorgid | fdataid,fuseorgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_barcm_scmodel_u |  | fdataid,fuseorgid |
| 2 | idx_t_barcm_scmodel_u_uo |  | fuseorgid |

---

## 源单列表配置-多语言表 t_barcm_scmodsrclist_l

- **表名称：** 源单列表配置-多语言表
- **表名：** t_barcm_scmodsrclist_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fmulsourcefield | fmulsourcefield | varchar | 80 |  | √ | ' ' |  |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 5 | fsfieldalias | 字段别名 | varchar | 255 |  | √ | ' ' | 字段别名 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_barcm_scmodsrclist_l_f |  | fentryid,flocaleid |
| 2 | pk_barcm_scmodsrclist_l |  | fpkid |

---

## 源单列表配置-子表 t_barcm_scmodsrclist

- **表名称：** 源单列表配置-子表
- **表名：** t_barcm_scmodsrclist

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmulsourcefield | fmulsourcefield | varchar | 80 |  | √ | ' ' |  |
| 3 | fsbdpropfieldsign | 基础资料属性标识 | varchar | 255 |  | √ | ' ' | 基础资料属性标识 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | flistdisplaystyle | 列表显示方式 | bpchar | 1 |  | √ | ' ' | 列表显示方式,枚举: A :不显示 B :原始数据 C :显示名称 D :显示编码/名称 E :基础资料属性 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fisfilter | 可过滤 | bpchar | 1 |  | √ | '0' | 可过滤 |
| 8 | fsfieldalias | 字段别名 | varchar | 255 |  | √ | ' ' | 字段别名 |
| 9 | fsourcefieldsign | 源单字段标识 | varchar | 80 |  | √ | ' ' | 源单字段标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_barcm_scmodtarset_fid |  | fid |
| 2 | pk_barcm_scmodsrclist |  | fentryid |
| 3 | idx_barcm_scmodsrclist_fid |  | fid |

---

## 插件-子表 t_barcm_scmodplugin

- **表名称：** 插件-子表
- **表名：** t_barcm_scmodplugin

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpluginpath | fpluginpath | varchar | 255 |  | √ | ' ' |  |
| 3 | fplugindescription | fplugindescription | varchar | 512 |  | √ | ' ' |  |
| 4 | fispluginpreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fscmodelpluginid | 扫描模型插件 | int8 | 64 |  | √ | 0 | [条码扫描模型插件管理 barcm_scanmodelplugin](../barcm_files/barcm_scanmodelplugin.md) |
| 7 | fisopen | 启用 | bpchar | 1 |  | √ | '0' | 启用 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fplugintype | fplugintype | bpchar | 1 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_barcm_scmodplugin_fid |  | fid |
| 2 | pk_barcm_scmodplugin |  | fentryid |

---

## 源单进度列表字段配置-多语言表 t_barcm_scmodsrclistp_l

- **表名称：** 源单进度列表字段配置-多语言表
- **表名：** t_barcm_scmodsrclistp_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fmulsourcefieldprogress | fmulsourcefieldprogress | varchar | 80 |  | √ | ' ' |  |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fsfieldaliasprogress | 字段别名 | varchar | 255 |  | √ | ' ' | 字段别名 |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_barcm_scmodsrclistp_l |  | fpkid |
| 2 | idx_barcm_scmodsrclistp_l_f |  | fentryid,flocaleid |

---

## 源单列表过滤分录-子表 t_barcm_scmodsrclistf

- **表名称：** 源单列表过滤分录-子表
- **表名：** t_barcm_scmodsrclistf

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffilterfield | 过滤字段基础资料 | int8 | 64 |  | √ | 0 | [PDA选单过滤字段 barcm_filterfields](../barcm_files/barcm_filterfields.md) |
| 3 | ffieldvisible | 是否显示 | bpchar | 1 |  | √ | '0' | 是否显示 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | barcm_scmlistf_idx |  | fid |
| 2 | pk_t_barcm_scmodsrclistf |  | fentryid |

---

## 目标单录入配置-子表 t_barcm_scmodtarset

- **表名称：** 目标单录入配置-子表
- **表名：** t_barcm_scmodtarset

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fisfieldpreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 3 | fmultargetfield | fmultargetfield | varchar | 80 |  | √ | ' ' |  |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fbcrulepropid | 条码属性项 | int8 | 64 |  | √ | 0 | [条码规则属性项 barcm_barcoderuleprop](../barcm_files/barcm_barcoderuleprop.md) |
| 6 | fisinputmemory | 录入记忆 | bpchar | 1 |  | √ | '0' | 录入记忆 |
| 7 | fismatchverify | 匹配校验 | bpchar | 1 |  | √ | '0' | 匹配校验 |
| 8 | fpdalock | PDA锁定性 | bpchar | 1 |  | √ | ' ' | PDA锁定性,枚举: A :按默认规则控制 B :强制可用 C :强制锁定 |
| 9 | fentrysign | 实体标识 | varchar | 80 |  | √ | ' ' | 实体标识 |
| 10 | fispropertychange | 是否触发PC值更新 | bpchar | 1 |  | √ | '0' | 是否触发PC值更新 |
| 11 | fbackfillbcmf | 回填主档 | bpchar | 1 |  | √ | '0' | 回填主档 |
| 12 | fispdavisible | PDA可见 | bpchar | 1 |  | √ | '0' | PDA可见 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 14 | ftargetfieldsign | 目标单字段标识 | varchar | 80 |  | √ | ' ' | 目标单字段标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_barcm_scmodtarset |  | fentryid |

---

## 条码扫描模型-分表 t_barcm_scmodel_a

- **表名称：** 条码扫描模型-分表
- **表名：** t_barcm_scmodel_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | freturntype | 退货类型 | bpchar | 1 |  | √ | ' ' | 退货类型,枚举: A :合格品退货 B :不合格品退货 |
| 3 | fsrcbillfilterjson | 源单列表过滤条件json | varchar | 255 |  | √ | ' ' | 源单列表过滤条件json |
| 4 | fsrcbillfilterjson_tag | 源单列表过滤条件json_详情 | text | 0 |  |  | null | 源单列表过滤条件json_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_barcm_scmodel_a |  | fid |
| 2 | idx_barcm_scmodela_fid |  | fid |

---

## 条码扫描模型-多语言表 t_barcm_scmodel_l

- **表名称：** 条码扫描模型-多语言表
- **表名：** t_barcm_scmodel_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | '0' |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fmobmeauname | 移动端菜单名 | varchar | 255 |  | √ | ' ' | 移动端菜单名 |
| 4 | fscenariodescription | 场景说明 | varchar | 255 |  | √ | ' ' | 场景说明 |
| 5 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_barcm_scmodel_l_fidflid |  | fid,flocaleid |
| 2 | pk_barcm_scmodel_l |  | fpkid |

---

## 源单进度列表字段配置-子表 t_barcm_scmodsrclistp

- **表名称：** 源单进度列表字段配置-子表
- **表名：** t_barcm_scmodsrclistp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsbdpropfieldsignprogress | 基础资料属性标识 | varchar | 255 |  | √ | ' ' | 基础资料属性标识 |
| 3 | fsourcefieldsignprogress | 源单字段标识 | varchar | 80 |  | √ | ' ' | 源单字段标识 |
| 4 | fmulsourcefieldprogress | fmulsourcefieldprogress | varchar | 80 |  | √ | ' ' |  |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | flistdisplaystyleprogress | 列表显示方式 | bpchar | 1 |  | √ | ' ' | 列表显示方式,枚举: A :不显示 B :原始数据 C :显示名称 D :显示编码/名称 E :基础资料属性 |
| 7 | fisfilterprogress | fisfilterprogress | bpchar | 1 |  | √ | '0' |  |
| 8 | fsfieldaliasprogress | 字段别名 | varchar | 255 |  | √ | ' ' | 字段别名 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_barcm_scmodtarsetp_fid |  | fid |
| 2 | pk_barcm_scmodsrclistp |  | fentryid |

---

## 条码扫描模型-主表 t_barcm_scmodel

- **表名称：** 条码扫描模型-主表
- **表名：** t_barcm_scmodel

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 分组 | int8 | 64 |  | √ | 0 | [条码扫描模型分组 barcm_scanmodelgroup](../barcm_files/barcm_scanmodelgroup.md) |
| 3 | fsrcbillfilterfieldsign | 源单查找字段标识 | varchar | 50 |  | √ | ' ' | 源单查找字段标识 |
| 4 | fisqtysrc | 携带源单数量 | bpchar | 1 |  | √ | '0' | 携带源单数量 |
| 5 | forgid | 管理组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fpermitemid | 权限项 | varchar | 80 |  | √ | ' ' | [权限项 perm_permitem](../base_files/perm_permitem.md) |
| 7 | fauthbizobjectid | 授权业务对象 | varchar | 80 |  | √ | ' ' | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |
| 8 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fseqnumber | 顺序号 | int8 | 64 |  | √ | 0 | 顺序号 |
| 11 | fconvertruleid | 转换规则 | varchar | 36 |  | √ | '0' | [转换规则 botp_crlist](../botp_files/botp_crlist.md) |
| 12 | fbitindex | fbitindex | int4 | 32 |  | √ | 0 |  |
| 13 | fconbindware | 容器绑定仓库仓位 | bpchar | 1 |  | √ | ' ' | 容器绑定仓库仓位,枚举: A :上架时绑定 B :下架时清除 |
| 14 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 15 | fmobmeauname | 移动端菜单名 | varchar | 255 |  | √ | ' ' | 移动端菜单名 |
| 16 | fmainbillmatch | 开启核心单据匹配 | bpchar | 1 |  | √ | '0' | 开启核心单据匹配 |
| 17 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 18 | fauthbizappid | 授权对象应用 | varchar | 80 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 19 | fmobbizobjid | 移动业务对象 | varchar | 80 |  | √ | ' ' | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |
| 20 | ftranstype | 调拨类型 | bpchar | 1 |  | √ | ' ' | 调拨类型,枚举: A :组织内调拨 B :跨组织调拨 |
| 21 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 22 | fnumber | 编号 | varchar | 80 |  | √ | ' ' | 编号 |
| 23 | fenableoptimization | 扫码性能优化 | bpchar | 1 |  | √ | '0' | 扫码性能优化 |
| 24 | fsourcebitindex | fsourcebitindex | int4 | 32 |  | √ | 0 |  |
| 25 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 26 | fisautogetsource | 根据条码自动获取源单数据 | bpchar | 1 |  | √ | '0' | 根据条码自动获取源单数据 |
| 27 | fmodeltype | 模型类型 | bpchar | 1 |  | √ | ' ' | 模型类型,枚举: A :有源单 B :无源单 C :专用模型 |
| 28 | fscenariodescription | 场景说明 | varchar | 512 |  | √ | ' ' | 场景说明 |
| 29 | ftargetbillstatus | 验货源单状态 | varchar | 10 |  | √ | ' ' | 验货源单状态,枚举: B :已提交 C :已审核 |
| 30 | fenableuploadattachment | 开启上传附件 | bpchar | 1 |  | √ | '0' | 开启上传附件 |
| 31 | fispreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 32 | ffifocontrol | 出库规则控制 | bpchar | 1 |  | √ | 'A' | 出库规则控制,枚举: A :不控制 B :按物料出库规则预警提示 C :按物料出库规则严格控制 |
| 33 | ficonpath | 图标路径 | varchar | 1000 |  | √ | ' ' | 图标路径 |
| 34 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 35 | finvschemeid | 目标库存事务 | int8 | 64 |  | √ | 0 | [库存事务 im_invscheme](../im_files/im_invscheme.md) |
| 36 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 37 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 38 | fsourcedataid | fsourcedataid | int8 | 64 |  | √ | 0 |  |
| 39 | fisgetinvqty | 盘点获取账存数量 | bpchar | 1 |  | √ | '0' | 盘点获取账存数量 |
| 40 | fisbackmainfile | 回填物料条码主档 | bpchar | 1 |  | √ | '0' | 回填物料条码主档 |
| 41 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 42 | fmodifierid | 修改人 | int8 | 64 |  |  | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 43 | fscautofindsrcbill | 扫码自动查找源单 | bpchar | 1 |  | √ | '0' | 扫码自动查找源单 |
| 44 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 45 | finvfiltertype | 进度查看库存过滤条件 | varchar | 10 |  | √ | ' ' | 进度查看库存过滤条件,枚举: A :按物料+界面仓库 B :按物料 |
| 46 | fsrcbillfilterfield | 源单查找字段 | varchar | 255 |  | √ | ' ' | 源单查找字段 |
| 47 | ftargetbilltypeid | 目标单据类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 48 | fisverifymode | 验货模式 | bpchar | 1 |  | √ | '0' | 验货模式 |
| 49 | fscanrecheck | 扫描复核 | bpchar | 1 |  | √ | '0' | 扫描复核 |
| 50 | ftargetbillid | 目标单 | varchar | 80 |  | √ | ' ' | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |
| 51 | fgenbillstatus | 目标单处理状态 | bpchar | 1 |  | √ | ' ' | 目标单处理状态,枚举: A :暂存 B :已提交 C :已审核 |
| 52 | fautogenbarcode | 自动创建调入条码主档 | bpchar | 1 |  | √ | '0' | 自动创建调入条码主档 |
| 53 | fisoutdeductmqty | 出库扣减主档数量 | bpchar | 1 |  | √ | '0' | 出库扣减主档数量 |
| 54 | fctrlstrategy | 控制策略 | varchar | 5 |  | √ | ' ' | 控制策略,枚举: 5 :全局共享 |
| 55 | ftargetbiztypeid | 目标业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 56 | fenablecheck | 物料复盘作业 | bpchar | 1 |  | √ | '0' | 物料复盘作业 |
| 57 | ffifocontrolrange | 出库规则控制范围 | bpchar | 1 |  | √ | ' ' | 出库规则控制范围,枚举: A :按仓库 B :按库存组织 |
| 58 | fsourcebillid | 源单 | varchar | 80 |  | √ | ' ' | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |
| 59 | fbizclassid | 业务分类 | int8 | 64 |  | √ | 0 | [条码业务分类 barcm_barcodebizclass](../barcm_files/barcm_barcodebizclass.md) |
| 60 | fignoreupdatevalue | 不触发PC值更新 | bpchar | 1 |  | √ | '0' | 不触发PC值更新 |
| 61 | fsrcbillorgfilter | 源单组织过滤条件 | varchar | 50 |  | √ | ' ' | 源单组织过滤条件,枚举: currentorg :按登录组织过滤 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_barcm_scmodel_number |  | fnumber |
| 2 | pk_barcm_scmodel |  | fid |
| 3 | idx_t_barcm_scmodel_createorg |  | fcreateorgid |
| 4 | idx_t_barcm_scmodel_master |  | fmasterid |

---

## 目标单列表配置-子表 t_barcm_scmodtarlist

- **表名称：** 目标单列表配置-子表
- **表名：** t_barcm_scmodtarlist

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmultargetlistfield | fmultargetlistfield | varchar | 80 |  | √ | ' ' |  |
| 3 | ftarlistdispstyle | 列表显示方式 | bpchar | 1 |  | √ | ' ' | 列表显示方式,枚举: A :不显示 B :原始数据 C :显示名称 D :显示编码/名称 E :基础资料属性 |
| 4 | ftfieldalias | 字段别名 | varchar | 255 |  | √ | ' ' | 字段别名 |
| 5 | ftargetlistfieldsign | 目标单列表字段标识 | varchar | 80 |  | √ | ' ' | 目标单列表字段标识 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | ftbdpropfieldsign | 基础资料属性标识 | varchar | 255 |  | √ | ' ' | 基础资料属性标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_barcm_scmodtarlist |  | fentryid |
| 2 | idx_barcm_scmodtarlist_fid |  | fid |

---

## 目标单列表配置-多语言表 t_barcm_scmodtarlist_l

- **表名称：** 目标单列表配置-多语言表
- **表名：** t_barcm_scmodtarlist_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fmultargetlistfield | fmultargetlistfield | varchar | 80 |  | √ | ' ' |  |
| 2 | ftfieldalias | 字段别名 | varchar | 255 |  | √ | ' ' | 字段别名 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_barcm_scmodtarlist_l_f |  | fentryid,flocaleid |
| 2 | pk_barcm_scmodtarlist_l |  | fpkid |
