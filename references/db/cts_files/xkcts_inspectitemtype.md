# 巡检业务分类-xkcts_inspectitemtype

## 单据体-多语言表 t_xkinsp_itemtypeentry_l

- **表名称：** 单据体-多语言表
- **表名：** t_xkinsp_itemtypeentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fname | 维度名称 | varchar | 50 |  | √ | ' ' | 维度名称 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fdescription | 说明 | varchar | 200 |  | √ | ' ' | 说明 |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkinsp_itemtypeentry_l |  | fpkid |
| 2 | idx_itemtypeentry_l |  | fentryid,flocaleid |

---

## 单据体-子表 t_xkinsp_itemtypeentry

- **表名称：** 单据体-子表
- **表名：** t_xkinsp_itemtypeentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 维度名称 | varchar | 50 |  | √ | ' ' | 维度名称 |
| 3 | ftype | 维度类型 | varchar | 1 |  | √ | ' ' | 维度类型,枚举: 1 :业务组织 2 :业务基础资料 |
| 4 | fbasetype | 基础资料类型 | varchar | 50 |  | √ | ' ' | 基础资料类型 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fplugin | 取值插件 | varchar | 200 |  | √ | ' ' | 取值插件 |
| 7 | fstrategy | 默认选择策略 | varchar | 1 |  | √ | ' ' | 默认选择策略,枚举: A :第一个 B :不限 |
| 8 | fdescription | 说明 | varchar | 200 |  | √ | ' ' | 说明 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fdefine | 维度定义 | varchar | 50 |  | √ | ' ' | 维度定义 |
| 11 | fcode | 维度编码 | varchar | 50 |  | √ | ' ' | 维度编码 |
| 12 | fbasenumber | 基础资料编码 | varchar | 50 |  | √ | ' ' | 基础资料编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkinsp_itemtypeentry |  | fentryid |
| 2 | idx_itemtypeentry_fid |  | fid,fseq |

---

## 巡检业务分类-多语言表 t_xkinsp_itemtype_l

- **表名称：** 巡检业务分类-多语言表
- **表名：** t_xkinsp_itemtype_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 200 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkinsp_itemtype_l |  | fid,flocaleid |
| 2 | pk_xkinsp_itemtype_l |  | fpkid |

---

## 巡检业务分类-主表 t_xkinsp_itemtype

- **表名称：** 巡检业务分类-主表
- **表名：** t_xkinsp_itemtype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fisapplyparam | 支持参数维度 | bpchar | 1 |  | √ | '1' | 支持参数维度 |
| 6 | fdescription | 描述 | varchar | 200 |  | √ | ' ' | 描述 |
| 7 | fappid | 所属应用 | varchar | 36 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | varchar | 50 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fissystem | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 13 | fenable | 可用状态 | bpchar | 1 |  | √ | '0' | 可用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkinsp_itemtype_num |  | fnumber |
| 2 | pk_xkinsp_itemtype |  | fid |
