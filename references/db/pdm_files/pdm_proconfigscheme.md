# 产品配置方案-pdm_proconfigscheme

## 产品配置方案-使用范围表 t_pdm_proconfigscheme_u

- **表名称：** 产品配置方案-使用范围表
- **表名：** t_pdm_proconfigscheme_u

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
| 1 | pk_t_pdm_proconfigscheme_u |  | fdataid,fuseorgid |
| 2 | idx_t_pdm_proconfigscheme_u_uo |  | fuseorgid |

---

## 产品配置方案-使用范围位图表 t_pdm_proconfigscheme_m

- **表名称：** 产品配置方案-使用范围位图表
- **表名：** t_pdm_proconfigscheme_m

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | forgid | forgid | int8 | 64 |  | √ | null |  |
| 2 | fdata | fdata | bytea | 0 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | forgid | forgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pdm_proconfigscheme_m |  | forgid |

---

## 产品配置方案-多语言表 t_pdm_proconfigscheme_l

- **表名称：** 产品配置方案-多语言表
- **表名：** t_pdm_proconfigscheme_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 配置方案名称 | varchar | 50 |  | √ | ' ' | 配置方案名称 |
| 3 | flocaleid | flocaleid | varchar | 255 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 255 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pdm_procmel_fid |  | fid,flocaleid |
| 2 | idx_pdm_procmel_fname |  | fname |
| 3 | pk_pdm_proconfigscheme_l |  | fpkid |

---

## 产品配置方案-主表 t_pdm_proconfigscheme

- **表名称：** 产品配置方案-主表
- **表名：** t_pdm_proconfigscheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fpriority | 优先级 | int8 | 64 |  | √ | 0 | 优先级 |
| 4 | fbomgroupid | 订单BOM分组 | int8 | 64 |  | √ | 0 | [BOM分组 mpdm_bomgroup](../mpdm_files/mpdm_bomgroup.md) |
| 5 | fmaterielfield | fmaterielfield | int8 | 64 |  | √ | 0 |  |
| 6 | fmaterielid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 7 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 9 | forderbom | forderbom | int8 | 64 |  | √ | 0 |  |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fdisabletime | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 12 | fmaterielnumrule | 物料编码规则 | varchar | 5 |  | √ | ' ' | 物料编码规则,枚举: 1 :物料编码规则 2 :自定义规则 |
| 13 | fradiogroupfield | fradiogroupfield | varchar | 5 |  | √ | ' ' |  |
| 14 | fstatus | 数据状态 | varchar | 5 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fmasterid | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 17 | fbomopentype | BOM展开方式 | varchar | 5 |  | √ | '3' | BOM展开方式,枚举: 1 :不展开 2 :仅可选件 3 :单级 4 :多级 |
| 18 | fcustomcoderuleid | 配置号规则 | int8 | 64 |  | √ | 0 | [配置号编码规则（废弃） bd_configcoderule](../sbd_files/bd_configcoderule.md) |
| 19 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 20 | finstantiation | 实例化物料 | varchar | 5 |  | √ | '2' | 实例化物料,枚举: 1 :是 2 :否 |
| 21 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 22 | fcodetype | 配置号编码方式 | varchar | 5 |  | √ | ' ' | 配置号编码方式,枚举: 1 :物料编码*流水号 2 :配置物料+销售订单 3 :自定义规则 |
| 23 | fconfigtype | 配置方式 | varchar | 5 |  | √ | '1' | 配置方式,枚举: 1 :组件选配 2 :特征选配 |
| 24 | fcreateorgid | 方案创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 25 | fdealresult | 配置结果处理 | varchar | 5 |  | √ | ' ' | 配置结果处理,枚举: 1 :产品配置清单 2 :订单BOM 3 :实例化物料BOM |
| 26 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 27 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 28 | fdisabletorid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 29 | fenabletorid | 启用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 30 | fmatcoderule | fmatcoderule | int8 | 64 |  | √ | 0 |  |
| 31 | forderbomid | 订单BOM类型 | int8 | 64 |  | √ | 0 | [BOM类型 mpdm_bomtype](../mpdm_files/mpdm_bomtype.md) |
| 32 | fctrlstrategy | 方案控制策略 | varchar | 5 |  | √ | '5' | 方案控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 33 | fenabletime | 启用时间 | timestamp | 0 |  |  | null | 启用时间 |
| 34 | fiscreateorderbom | fiscreateorderbom | varchar | 5 |  | √ | '1' |  |
| 35 | fisrepeatbom | 匹配相同配置 | varchar | 5 |  | √ | ' ' | 匹配相同配置 |
| 36 | fsuperbomid | 超级BOM类型 | int8 | 64 |  | √ | 0 | [BOM类型 mpdm_bomtype](../mpdm_files/mpdm_bomtype.md) |
| 37 | fenable | 使用状态 | varchar | 5 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 38 | fnumber | 配置方案编号 | varchar | 30 |  | √ | ' ' | 配置方案编号 |
| 39 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 40 | fmaterialcoderule | 实例化物料编码规则 | varchar | 64 |  | √ | ' ' | [编码规则 bos_coderule](../base_files/bos_coderule.md) |
| 41 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pdm_proconfigscheme |  | fid |
| 2 | idx_pdm_procme_fnumber |  | fnumber |
| 3 | idx_t_pdm_proconfigscheme_createorg |  | fcreateorgid |
| 4 | idx_t_pdm_proconfigscheme_master |  | fmasterid |
| 5 | idx_pdm_procme_fcreatetime |  | fcreatetime |

---

## 特征信息-子表 t_pdm_featureinfo

- **表名称：** 特征信息-子表
- **表名：** t_pdm_featureinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffeatureruleid | ffeatureruleid | int8 | 64 |  | √ | 0 |  |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | ffeatureid | 特征编码 | int8 | 64 |  | √ | 0 | [特征定义 pdm_featuredefinition](../pdm_files/pdm_featuredefinition.md) |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pdm_featfo_fid |  | fid |
| 2 | idx_pdm_featfo_fseq |  | fseq |
| 3 | pk_pdm_featureinfo |  | fentryid |

---

## 配置规则-子表 t_pdm_featureruleentry

- **表名称：** 配置规则-子表
- **表名：** t_pdm_featureruleentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | ffeaturerule | 特征规则编码 | int8 | 64 |  | √ | 0 | [配置规则 pdm_chararule](../pdm_files/pdm_chararule.md) |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_pdm_featureruleentry |  | ffeaturerule |
| 2 | pk_t_pdm_featureruleentry |  | fdetailid |
