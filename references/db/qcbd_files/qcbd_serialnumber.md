# 序列号记录-qcbd_serialnumber

## 序列号记录-多语言表 t_qcbd_serialnumberrecord_l

- **表名称：** 序列号记录-多语言表
- **表名：** t_qcbd_serialnumberrecord_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  |  | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_qcbd_serialnumberrecord_l |  | fpkid |

---

## 序列号记录-主表 t_qcbd_serialnumberrecord

- **表名称：** 序列号记录-主表
- **表名：** t_qcbd_serialnumberrecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fissecondused | 是否被二次检验使用（F7二次检验过滤的时候排除掉） | bpchar | 1 |  | √ | '0' | 是否被二次检验使用（F7二次检验过滤的时候排除掉） |
| 3 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 4 | fsrcentryid | 来源分录id | varchar | 100 |  | √ | ' ' | 来源分录id |
| 5 | fsrcbillid | 来源单据id | varchar | 100 |  | √ | ' ' | 来源单据id |
| 6 | fisselect | 是否挑选处理方式 | bpchar | 1 |  | √ | '0' | 是否挑选处理方式 |
| 7 | fisusedinspect | 序列号是否被检验单使用 | bpchar | 1 |  | √ | '0' | 序列号是否被检验单使用 |
| 8 | fsrcentrykey | 来源单据分录标识 | varchar | 100 |  | √ | ' ' | 来源单据分录标识 |
| 9 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fusedinspectid | 序列号被使用检验单（不良品单）对象ID | int8 | 64 |  | √ | 0 | 序列号被使用检验单（不良品单）对象ID |
| 12 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 13 | fmaterial | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 14 | fnumber | 序列号显示 | varchar | 100 |  | √ | ' ' | 序列号显示 |
| 15 | fsnnumber | 序列号 | varchar | 100 |  | √ | ' ' | 序列号 |
| 16 | fsrcbilltype | 来源单据类型 | varchar | 100 |  | √ | ' ' | 来源单据类型 |
| 17 | fsnnumbermasterid | 序列号主键ID | varchar | 100 |  | √ | ' ' | 序列号主键ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_qcbd_serialnumberrecord |  | fsnnumbermasterid |
| 2 | pk_qcbd_serialnumberrecord |  | fid |
