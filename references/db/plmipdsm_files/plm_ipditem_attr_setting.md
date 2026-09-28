# 工作项类型设置-属性属性-plm_ipditem_attr_setting

## 单据体-多语言表 t_plm_pm_projectattrentry_l

- **表名称：** 单据体-多语言表
- **表名：** t_plm_pm_projectattrentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fothername | 别名 | varchar | 80 |  | √ | ' ' | 别名 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_pm_projectattrentry_l |  | fpkid |
| 2 | idx_plm_pm_proattrentry_l_0 |  | fentryid,flocaleid |

---

## 工作项类型设置-属性属性-主表 t_plm_pm_projectattr

- **表名称：** 工作项类型设置-属性属性-主表
- **表名：** t_plm_pm_projectattr

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcreateorgid | 创建组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 2 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 3 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 5 | fuseorg | 业务组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fentitykey | 实体标识 | varchar | 50 |  | √ | ' ' | 实体标识 |
| 9 | fprojectkind | 类型 | varchar | 50 |  | √ | ' ' | 类型 |
| 10 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 11 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  |  | null | 主数据内码 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fsourcedataid | 原资料id | int8 | 64 |  |  | null | 原资料id |
| 17 | fbitindex | 位图 | int8 | 64 |  |  | null | 位图 |
| 18 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 19 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 20 | fsourcebitindex | 原资料位图 | int8 | 64 |  |  | null | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_pm_projectattr |  | fid |
| 2 | idx_plm_pm_projectattr_m0 |  | fmasterid |
| 3 | idx_t_plm_pm_projectattr_master |  | fmasterid |
| 4 | idx_t_plm_pm_projectattr_createorg |  | fcreateorgid |

---

## 单据体-子表 t_plm_pm_projectattrentry

- **表名称：** 单据体-子表
- **表名：** t_plm_pm_projectattrentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | freadonlyenable | 只读是否可编辑 | bpchar | 1 |  | √ | '0' | 只读是否可编辑 |
| 3 | flistshow | 列表显示 | bpchar | 1 |  | √ | '0' | 列表显示 |
| 4 | fothernameenable | 别名是否可编辑 | bpchar | 1 |  | √ | '0' | 别名是否可编辑 |
| 5 | fextendenable | 继承是否可编辑 | bpchar | 1 |  | √ | '0' | 继承是否可编辑 |
| 6 | fbasedatainfo | 基础资料详情 | varchar | 2000 |  | √ | ' ' | 基础资料详情 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | frequiredenable | 必填是否可编辑 | bpchar | 1 |  | √ | '0' | 必填是否可编辑 |
| 9 | frequired | 必填 | bpchar | 1 |  | √ | '0' | 必填 |
| 10 | fdefault | 默认值 | varchar | 512 |  | √ | ' ' | 默认值 |
| 11 | feditshowenable | 显示是否可编辑 | bpchar | 1 |  | √ | '0' | 显示是否可编辑 |
| 12 | fattrgroupenable | 属性分组是否可编辑 | bpchar | 1 |  | √ | '0' | 属性分组是否可编辑 |
| 13 | fkey | 字段标识 | varchar | 50 |  | √ | ' ' | 字段标识 |
| 14 | fisext | 自定义字段 | bpchar | 1 |  | √ | '0' | 自定义字段 |
| 15 | fdefaultenable | 默认值是否可编辑 | bpchar | 1 |  | √ | '0' | 默认值是否可编辑 |
| 16 | fbaseinfovalue | 基础资料信息 | varchar | 255 |  | √ | ' ' | 基础资料信息 |
| 17 | fattrfield | 属性字段 | varchar | 50 |  | √ | ' ' | 属性字段 |
| 18 | feditshow | 显示 | bpchar | 1 |  | √ | '0' | 显示 |
| 19 | fextend | 继承 | bpchar | 1 |  | √ | '0' | 继承 |
| 20 | fothername | 别名 | varchar | 50 |  | √ | ' ' | 别名 |
| 21 | ffieldtypeid | 字段类型id | varchar | 50 |  | √ | ' ' | 字段类型id |
| 22 | fbaseinfovalue_tag | 基础资料信息_详情 | text | 0 |  |  | null | 基础资料信息_详情 |
| 23 | freadonly | 只读 | bpchar | 1 |  | √ | '0' | 只读 |
| 24 | ffieldtype | 字段类型 | varchar | 50 |  | √ | ' ' | 字段类型 |
| 25 | fisdefine | 是否自定义 | bpchar | 1 |  | √ | '0' | 是否自定义 |
| 26 | fattrgroup | 属性分组 | int8 | 64 |  |  | null | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 27 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_pm_projectattrentry |  | fentryid |
| 2 | idx_plm_pm_projectattrentry_fk |  | fid |

---

## 工作项类型设置-属性属性-多语言表 t_plm_pm_projectattr_l

- **表名称：** 工作项类型设置-属性属性-多语言表
- **表名：** t_plm_pm_projectattr_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_pm_projectattr_l_0 |  | fid,flocaleid |
| 2 | pk_plm_pm_projectattr_l |  | fpkid |

---

## 工作项类型设置-属性属性-使用范围表 t_plm_pm_projectattr_u

- **表名称：** 工作项类型设置-属性属性-使用范围表
- **表名：** t_plm_pm_projectattr_u

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
| 1 | pk_t_plm_pm_projectattr_u |  | fdataid,fuseorgid |
| 2 | idx_t_plm_pm_projectattr_u_uo |  | fuseorgid |
