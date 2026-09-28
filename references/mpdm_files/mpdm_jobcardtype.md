# 工卡类型-mpdm_jobcardtype

## 工卡类型-多语言表 t_mpdm_jobcardtype_l

- **表名称：** 工卡类型-多语言表
- **表名：** t_mpdm_jobcardtype_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 20 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_mpdm_jobctype_l |  | fid,flocaleid |
| 2 | pk_t_mpdm_jobcardtype_l |  | fpkid |

---

## 工卡类型-主表 t_mpdm_jobcardtype

- **表名称：** 工卡类型-主表
- **表名：** t_mpdm_jobcardtype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fprocesstype | 工艺类型 | varchar | 50 |  | √ | ' ' | 工艺类型,枚举: A :物料 B :物料组 C :通用 D :检修设备类型 E :例行 |
| 6 | fissyspre | 预设 | bpchar | 1 |  | √ | ' ' | 预设 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fworktypectrlid | 工卡类型 | int8 | 64 |  | √ | 0 | 工卡类型控制 mpdm_worktypectrl |
| 9 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fisproductrequired | 产品必填 | bpchar | 1 |  | √ | ' ' | 产品必填 |
| 13 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 15 | fcombofield | 快照生成维度 | varchar | 50 |  | √ | ' ' | 快照生成维度,枚举: A :全部 B :客户工卡版本号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_jobcardtype_fnumber |  | fnumber |
| 2 | pk_t_mpdm_jobcardtype |  | fid |
