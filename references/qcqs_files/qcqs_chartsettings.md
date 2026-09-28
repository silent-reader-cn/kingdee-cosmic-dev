# 图表设置(废弃)-qcqs_chartsettings

## 图表设置(废弃)-主表 t_qcbd_chartset

- **表名称：** 图表设置(废弃)-主表
- **表名：** t_qcbd_chartset

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fchartindex | 图表数 | int8 | 64 |  | √ | 0 | 图表数 |
| 4 | fformkey | 表单标识 | varchar | 80 |  | √ | ' ' | 表单标识 |
| 5 | fsettingstr | 设置项详情 | varchar | 255 |  | √ | ' ' | 设置项详情 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fsettingdetail_tag | 设置详情_详情 | text | 0 |  |  | ' ' | 设置详情_详情 |
| 8 | fsettingdetail | 设置详情 | varchar | 255 |  | √ | ' ' | 设置详情 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fsettingstr_tag | 设置项详情_详情 | text | 0 |  |  | ' ' | 设置项详情_详情 |
| 14 | fchecked | 选择 | bpchar | 1 |  | √ | '0' | 选择 |
| 15 | fenable | 使用状态 | varchar | 5 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 16 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 17 | fsettingname | 设置名称 | varchar | 80 |  | √ | ' ' | 设置名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_qcbd_cset_fnumber |  | fnumber |
| 2 | pk_qcbd_chartset |  | fid |

---

## 图表设置(废弃)-多语言表 t_qcbd_chartset_l

- **表名称：** 图表设置(废弃)-多语言表
- **表名：** t_qcbd_chartset_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | ffullname | ffullname | varchar | 100 |  | √ | ' ' |  |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_qcbd_chartset_l |  | fpkid |
| 2 | idx_qcbd_chasetl_fid |  | fid,flocaleid |
