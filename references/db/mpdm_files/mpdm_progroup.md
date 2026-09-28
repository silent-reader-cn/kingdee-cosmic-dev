# 工序组(废弃)-mpdm_progroup

## 工序组(废弃)-多语言表 t_mpdm_progroup_l

- **表名称：** 工序组(废弃)-多语言表
- **表名：** t_mpdm_progroup_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | ffullname | 长名称 | varchar | 500 |  | √ | ' ' | 长名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpdm_progroup_l |  | fid,flocaleid |
| 2 | t_mpdm_progroup_l_pkey |  | fpkid |

---

## 工序组(废弃)-主表 t_mpdm_progroup

- **表名称：** 工序组(废弃)-主表
- **表名：** t_mpdm_progroup

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fisleaf | 是否叶子 | bpchar | 1 |  | √ | '1' | 是否叶子 |
| 5 | fname | fname | varchar | 60 |  | √ | ' ' |  |
| 6 | fismronrc | 适用于非例行工卡 | bpchar | 1 |  | √ | '0' | 适用于非例行工卡 |
| 7 | fparentid | 上级分组 | int8 | 64 |  | √ | 0 | 工序组(废弃) mpdm_progroup |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | flongnumber | 长编码 | varchar | 255 |  | √ | ' ' | 长编码 |
| 10 | fparenttypeid | fparenttypeid | int8 | 64 |  | √ | 0 |  |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | flevel | 级次 | int8 | 64 |  | √ | 0 | 级次 |
| 14 | fscoperange | 适用工卡范围 | varchar | 50 |  | √ | ' ' | 适用工卡范围,枚举: A :适用标准工卡 B :适用非例行工卡 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 17 | fdefaultworksort | 默认工作顺序 | int8 | 64 |  | √ | 0 | 默认工作顺序 |
| 18 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 19 | fnumber | 编码 | varchar | 60 |  | √ | ' ' | 编码 |
| 20 | fpaneltimetype | 面板工时类型 | varchar | 50 |  | √ | ' ' | 面板工时类型,枚举: A :拆卸 B :安装 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpdm_progroup_fnumber |  | fnumber |
| 2 | t_mpdm_progroup_pkey |  | fid |

---

## 适用工卡范围（废弃）-多选基础资料表 t_mpdm_progroupscoperange

- **表名称：** 适用工卡范围（废弃）-多选基础资料表
- **表名：** t_mpdm_progroupscoperange

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | varchar | 36 |  | √ | ' ' | 工卡类型 mpdm_jobcardtype |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpdm_progroupscoperange |  | fpkid |
| 2 | idx_mpdm_progroupscoperange_fk |  | fid |
