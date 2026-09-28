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
| 6 | fscmodelpluginid | 扫描模型插件 | int8 | 64 |  | √ | 0 | 条码扫描模型插件管理 barcm_scanmodelplugin |
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
| 5 | fbcrulepropid | 条码属性项 | int8 | 64 |  | √ | 0 | 条码规则属性项 barcm_barcoderuleprop |
| 6 | fisinputmemory | 录入记忆 | bpchar | 1 |  | √ | '0' | 录入记忆 |
| 7 | fismatchverify | 匹配校验 | bpchar | 1 |  | √ | '0' | 匹配校验 |
| 8 | fpdalock | PDA锁定性 | bpchar | 1 |  | √ | ' ' | PDA锁定性,枚举: A :按默认规则控制 B :强制可用 C :强制锁定 |
| 9 | fentrysign | 实体标识 | varchar | 80 |  | √ | ' ' | 实体标识 |
| 10 | fbackfillbcmf | 回填主档 | bpchar | 1 |  | √ | '0' | 回填主档 |
| 11 | fispdavisible | PDA可见 | bpchar | 1 |  | √ | '0' | PDA可见 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | ftargetfieldsign | 目标单字段标识 | varchar | 80 |  | √ | ' ' | 目标单字段标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_barcm_scmodtarset |  | fentryid |

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

## 条码扫描模型-主表 t_barcm_scmodel

- **表名称：** 条码扫描模型-主表
- **表名：** t_barcm_scmodel

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 分组 | int8 | 64 |  | √ | 0 | 条码扫描模型分组 barcm_scanmodelgroup |
| 3 | forgid | 管理组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fpermitemid | 权限项 | varchar | 80 |  | √ | ' ' | 权限项 perm_permitem |
| 5 | fauthbizobjectid | 授权业务对象 | varchar | 80 |  | √ | ' ' | 业务对象 bos_objecttype |
| 6 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fseqnumber | 顺序号 | int8 | 64 |  | √ | 0 | 顺序号 |
| 9 | fconvertruleid | 转换规则 | varchar | 36 |  | √ | '0' | 转换规则 botp_crlist |
| 10 | fbitindex | fbitindex | int4 | 32 |  | √ | 0 |  |
| 11 | fconbindware | 容器绑定仓库仓位 | bpchar | 1 |  | √ | ' ' | 容器绑定仓库仓位,枚举: A :上架时绑定 B :下架时清除 |
| 12 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 13 | fmobmeauname | 移动端菜单名 | varchar | 255 |  | √ | ' ' | 移动端菜单名 |
| 14 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 15 | fauthbizappid | 授权对象应用 | varchar | 80 |  | √ | ' ' | 业务应用实体 bos_devportal_bizapp |
| 16 | fmobbizobjid | 移动业务对象 | varchar | 80 |  | √ | ' ' | 业务对象 bos_objecttype |
| 17 | ftranstype | 调拨类型 | bpchar | 1 |  | √ | ' ' | 调拨类型,枚举: A :组织内调拨 B :跨组织调拨 |
| 18 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 19 | fnumber | 编号 | varchar | 80 |  | √ | ' ' | 编号 |
| 20 | fsourcebitindex | fsourcebitindex | int4 | 32 |  | √ | 0 |  |
| 21 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 22 | fisautogetsource | 根据条码自动获取源单数据 | bpchar | 1 |  | √ | '0' | 根据条码自动获取源单数据 |
| 23 | fmodeltype | 模型类型 | bpchar | 1 |  | √ | ' ' | 模型类型,枚举: A :有源单 B :无源单 C :专用模型 |
| 24 | fscenariodescription | 场景说明 | varchar | 512 |  | √ | ' ' | 场景说明 |
| 25 | fispreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 26 | ffifocontrol | 出库规则控制 | bpchar | 1 |  | √ | 'A' | 出库规则控制,枚举: A :不控制 B :按物料出库规则预警提示 C :按物料出库规则严格控制 |
| 27 | ficonpath | 图标路径 | varchar | 1000 |  | √ | ' ' | 图标路径 |
| 28 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 29 | finvschemeid | 目标库存事务 | int8 | 64 |  | √ | 0 | 库存事务 im_invscheme |
| 30 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 31 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 32 | fsourcedataid | fsourcedataid | int8 | 64 |  | √ | 0 |  |
| 33 | fisbackmainfile | 回填物料条码主档 | bpchar | 1 |  | √ | '0' | 回填物料条码主档 |
| 34 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 35 | fmodifierid | 修改人 | int8 | 64 |  |  | 0 | 人员 bos_user |
| 36 | fscautofindsrcbill | 扫码自动查找源单 | bpchar | 1 |  | √ | '0' | 扫码自动查找源单 |
| 37 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 38 | ftargetbilltypeid | 目标单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 39 | fisverifymode | 验货模式 | bpchar | 1 |  | √ | '0' | 验货模式 |
| 40 | ftargetbillid | 目标单 | varchar | 80 |  | √ | ' ' | 业务对象 bos_objecttype |
| 41 | fgenbillstatus | 目标单处理状态 | bpchar | 1 |  | √ | ' ' | 目标单处理状态,枚举: A :暂存 B :已提交 C :已审核 |
| 42 | fautogenbarcode | 自动创建调入条码主档 | bpchar | 1 |  | √ | '0' | 自动创建调入条码主档 |
| 43 | fisoutdeductmqty | 出库扣减主档数量 | bpchar | 1 |  | √ | '0' | 出库扣减主档数量 |
| 44 | fctrlstrategy | 控制策略 | bpchar | 3 |  | √ | ' ' | 控制策略,枚举: 5 :全局共享 |
| 45 | ftargetbiztypeid | 目标业务类型 | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 46 | fenablecheck | 物料复盘作业 | bpchar | 1 |  | √ | '0' | 物料复盘作业 |
| 47 | ffifocontrolrange | 出库规则控制范围 | bpchar | 1 |  | √ | ' ' | 出库规则控制范围,枚举: A :按仓库 B :按库存组织 |
| 48 | fsourcebillid | 源单 | varchar | 80 |  | √ | ' ' | 业务对象 bos_objecttype |
| 49 | fbizclassid | 业务分类 | int8 | 64 |  | √ | 0 | 条码业务分类 barcm_barcodebizclass |

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
