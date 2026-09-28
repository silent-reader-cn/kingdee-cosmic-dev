# 核销类别-msmod_writeofftype

## 核销类别-多语言表 t_msmod_writeofftype_l

- **表名称：** 核销类别-多语言表
- **表名：** t_msmod_writeofftype_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 512 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_msmod_writeofftype_l_id |  | fid,flocaleid |
| 2 | pk_t_msmod_writeofftype_l |  | fpkid |

---

## 分摊面板-子表 t_msmod_shareentity_e

- **表名称：** 分摊面板-子表
- **表名：** t_msmod_shareentity_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | fsharefield | 分摊标准字段 | varchar | 50 |  | √ | ' ' | 分摊标准字段 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | fsharewfbilltypeid | 核销单据 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 6 | fsharefieldkey | 分摊标准字段Key | varchar | 50 |  | √ | ' ' | 分摊标准字段Key |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msmod_shareentity_e_fid |  | fid |
| 2 | pk_t_msmod_shareentity_e |  | fentryid |

---

## 核销单据-子表 t_msmod_wfbillsetentry

- **表名称：** 核销单据-子表
- **表名：** t_msmod_wfbillsetentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fwholefieldkey | 完全核销字段 | varchar | 50 |  | √ | ' ' | 完全核销字段 |
| 3 | fisautogenerate | 自动生成 | bpchar | 1 |  | √ | '0' | 自动生成 |
| 4 | fismainshare | 分摊主方 | bpchar | 1 |  | √ | '0' | 分摊主方 |
| 5 | ffiltercondition_tag | 过滤条件有效值_详情 | text | 0 |  |  | null | 过滤条件有效值_详情 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fwriteoffbillname | 核销单据名称 | varchar | 50 |  | √ | ' ' | 核销单据名称 |
| 8 | fwfbillalias | 核销单据标识 | int8 | 64 |  | √ | 0 | [核销单据类型 msmod_billtype](../mscommon_files/msmod_billtype.md) |
| 9 | fcfiltercondition_tag | 追加过滤条件有效值_详情 | text | 0 |  |  | null | 追加过滤条件有效值_详情 |
| 10 | ffilterconditionview | 过滤条件 | varchar | 512 |  | √ | ' ' | 过滤条件 |
| 11 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 12 | fwfmapping | 核销记录映射配置 | int8 | 64 |  | √ | 0 | [通用映射配置 sbs_billfieldmapping](../mscommon_files/sbs_billfieldmapping.md) |
| 13 | fwriteoffbillnumber | 核销单据编码 | varchar | 80 |  | √ | ' ' | 核销单据编码 |
| 14 | fstatus | fstatus | bpchar | 1 |  | √ | ' ' |  |
| 15 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 16 | fmasterid | fmasterid | int8 | 64 |  | √ | 0 |  |
| 17 | fwriteoffbilltypeid | 核销单据 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 18 | ffiltercondition | 过滤条件有效值 | varchar | 255 |  | √ | ' ' | 过滤条件有效值 |
| 19 | fcfilterconditionview | 追加过滤条件 | varchar | 512 |  | √ | ' ' | 追加过滤条件 |
| 20 | fcfiltercondition | 追加过滤条件有效值 | varchar | 255 |  | √ | ' ' | 追加过滤条件有效值 |
| 21 | fisdeletelautobill | fisdeletelautobill | bpchar | 1 |  | √ | '0' |  |
| 22 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 23 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'C' | 单据状态,枚举: A :创建 B :审核中 C :已审核 D :重新审核 |
| 24 | fwholefieldname | 完全核销字段名称 | varchar | 50 |  | √ | ' ' | 完全核销字段名称 |
| 25 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 26 | fisinvolved | 参与核销 | bpchar | 1 |  | √ | '1' | 参与核销 |
| 27 | fwriteoffbilltenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 28 | ffilterconditiondesc | 过滤条件详情(JSON) | varchar | 255 |  | √ | ' ' | 过滤条件详情(JSON) |
| 29 | frbwriteoff | 红蓝核销 | bpchar | 1 |  | √ | '0' | 红蓝核销 |
| 30 | fwriteofftypenumber | 核销类别编码 | varchar | 80 |  | √ | ' ' | 核销类别编码 |
| 31 | frbwfmapping | 红蓝核销记录映射 | int8 | 64 |  | √ | 0 | [通用映射配置 sbs_billfieldmapping](../mscommon_files/sbs_billfieldmapping.md) |
| 32 | ffilterconditiondesc_tag | 过滤条件详情(JSON)_详情 | text | 0 |  |  | null | 过滤条件详情(JSON)_详情 |
| 33 | fcfilterconditiondesc | 追加过滤条件详情(JSON) | varchar | 255 |  | √ | ' ' | 追加过滤条件详情(JSON) |
| 34 | fnumber | fnumber | varchar | 80 |  | √ | ' ' |  |
| 35 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 36 | falias | 核销单据标识 | varchar | 50 |  | √ | ' ' | 核销单据标识 |
| 37 | fcfilterconditiondesc_tag | 追加过滤条件详情(JSON)_详情 | text | 0 |  |  | null | 追加过滤条件详情(JSON)_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_msmod_wfbillsetentry |  | fentryid |
| 2 | idx_fwriteoffbilltypeid |  | fwriteoffbilltypeid |
| 3 | idx_wfbillsetentry_fid |  | fid |

---

## 核销类别-主表 t_msmod_writeofftype

- **表名称：** 核销类别-主表
- **表名：** t_msmod_writeofftype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fisfeeshare | 核销采用分摊算法 | bpchar | 1 |  | √ | '0' | 核销采用分摊算法 |
| 4 | fbizapp | 所属应用 | varchar | 36 |  | √ | ' ' | [业务应用列表 bos_devp_bizapplist](../devnew_files/bos_devp_bizapplist.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fispreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fwriteoffplugin | 核销插件 | varchar | 255 |  | √ | ' ' | 核销插件 |
| 12 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 13 | fwriteoffrecordbillid | 核销记录存储 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 14 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 15 | fwriteofftype | 核销类型 | varchar | 5 |  | √ | 'A' | 核销类型,枚举: A :核销 B :费用分摊 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_msmod_writeofftype_num |  | fnumber |
| 2 | pk_t_msmod_writeofftype |  | fid |

---

## 核销字段-子表 t_msmod_wffieldsubentry

- **表名称：** 核销字段-子表
- **表名：** t_msmod_wffieldsubentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcalculationrule | 取反 | varchar | 50 |  | √ | ' ' | 取反 |
| 2 | fwriteoffcalcfield | 核销主字段 | bpchar | 1 |  | √ | '0' | 核销主字段 |
| 3 | fcalformuladesc_tag | 计算公式json描述_详情 | text | 0 |  |  | null | 计算公式json描述_详情 |
| 4 | fvaluemethod | 取值方式 | varchar | 5 |  | √ | 'A' | 取值方式,枚举: A :源单字段 C :动态字段 |
| 5 | fwriteofffieldname | 核销字段名称 | varchar | 50 |  | √ | ' ' | 核销字段名称 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fwffieldplugin | 动态字段 | varchar | 255 |  | √ | ' ' | 动态字段,枚举: curqty :本次核销数量 curbaseqty :本次核销基本数量 curamount :本次核销金额 unwfamount :未核销金额 unwfqty :未核销数量 qty :数量 amount :金额 |
| 8 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 9 | fwriteofffieldkey | 核销字段 | varchar | 50 |  | √ | ' ' | 核销字段 |
| 10 | fcalformuladesc | 计算公式json描述 | varchar | 255 |  | √ | ' ' | 计算公式json描述 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 12 | fwffieldformula | 核销字段计算公式 | varchar | 50 |  | √ | ' ' | 核销字段计算公式 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fentryid |  | fentryid |
| 2 | pk_t_msmod_wffieldsubentry |  | fdetailid |

---

## 插件列表-子表 t_msmod_pluginentity_e

- **表名称：** 插件列表-子表
- **表名：** t_msmod_pluginentity_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpluginclass | 插件实现类 | varchar | 255 |  | √ | ' ' | 插件实现类 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fpeispreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fplugindesc | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 7 | fplugintype | 插件类别 | bpchar | 1 |  | √ | ' ' | 插件类别,枚举: 1 :核销插件 2 :反核销插件 3 :过滤插件 4 :匹配插件 5 :反写插件 6 :其他插件 |
| 8 | fpluginenabled | 启用 | bpchar | 1 |  | √ | '1' | 启用 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msmod_pluginentity_e_fid |  | fid |
| 2 | pk_t_msmod_pluginentity_e |  | fentryid |

---

## 自动生成单据-子表 t_msmod_autogenebill_e

- **表名称：** 自动生成单据-子表
- **表名：** t_msmod_autogenebill_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fisdeletefilterdesc | 删除条件过滤详情 | varchar | 255 |  | √ | ' ' | 删除条件过滤详情 |
| 3 | fwfbeispreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 4 | ftargetbilltypeid | 目标单据 | varchar | 36 |  | √ | ' ' | 目标单据,枚举: |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fbotpruleid | BOTP规则 | varchar | 50 |  | √ | ' ' | [转换规则 botp_crlist](../botp_files/botp_crlist.md) |
| 7 | fisdeletefilter | 反核销删除条件 | varchar | 512 |  | √ | ' ' | 反核销删除条件 |
| 8 | fautoplugin | fautoplugin | varchar | 255 |  | √ | ' ' |  |
| 9 | fisdeletefilterdesc_tag | 删除条件过滤详情_详情 | text | 0 |  |  | null | 删除条件过滤详情_详情 |
| 10 | ftargetbilltype | 目标单据 | int8 | 64 |  | √ | 0 | [核销单据类型 msmod_billtype](../mscommon_files/msmod_billtype.md) |
| 11 | fsrcbilltype | 来源单据 | int8 | 64 |  | √ | 0 | [核销单据类型 msmod_billtype](../mscommon_files/msmod_billtype.md) |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | fsrcbilltypeid | 来源单据 | varchar | 36 |  | √ | ' ' | 来源单据,枚举: |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_msmod_autogenebill_e_fid |  | fid |
| 2 | pk_t_msmod_autogenebill_e |  | fentryid |
