# 面板定义-mpdm_paneldef

## 拆装工时信息-子表 t_mpdm_paneltimes

- **表名称：** 拆装工时信息-子表
- **表名：** t_mpdm_paneltimes

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fprogroup | 工序组 | int8 | 64 |  | √ | 0 | 工序组(废弃) mpdm_progroup |
| 3 | fworkhours | 工时(小时) | numeric | 23 | 10 | √ | 0 | 工时(小时) |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fmajor | 行业 | int8 | 64 |  | √ | 0 | 树形基础资料模板 mpdm_professiona |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpdm_paneltimes |  | fentryid |
| 2 | idx_mpdm_paneltimes_fk |  | fid |

---

## 面板定义-主表 t_mpdm_paneldef

- **表名称：** 面板定义-主表
- **表名：** t_mpdm_paneldef

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fdescribe | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 6 | fmaterialtype | 检修设备类型 | int8 | 64 |  | √ | 0 | 检修设备类型 mpdm_mrtype |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: C :已审核 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 12 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 13 | ffunctionlocation | 功能位置 | int8 | 64 |  | √ | 0 | 功能位置 mpdm_functionlocation |
| 14 | funit | 工时单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | mpdm_panel_fmasterid_idx |  | fmasterid |
| 2 | pk_mpdm_paneldef |  | fid |

---

## 面板定义-多语言表 t_mpdm_paneldef_l

- **表名称：** 面板定义-多语言表
- **表名：** t_mpdm_paneldef_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpdm_paneldef_l_0 |  | fid,flocaleid |
| 2 | pk_mpdm_paneldef_l |  | fpkid |
