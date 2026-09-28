# 招标项目信息变更-src_projectinfo_chg

## 招标项目信息变更-多语言表 t_src_projectinfochg_l

- **表名称：** 招标项目信息变更-多语言表
- **表名：** t_src_projectinfochg_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fnewbidname | 招标项目名称(变更后) | varchar | 300 |  | √ | ' ' | 招标项目名称(变更后) |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |
| 5 | fbidname | 招标项目名称(变更前) | varchar | 300 |  | √ | ' ' | 招标项目名称(变更前) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_projectinfochg_l |  | fpkid |
| 2 | idx_src_proinfochg_l_flocaleid |  | flocaleid |

---

## 招标项目信息变更-主表 t_src_projectinfochg

- **表名称：** 招标项目信息变更-主表
- **表名：** t_src_projectinfochg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbidchangeid | 寻源项目变更F7 | int8 | 64 |  | √ | 0 | 寻源项目变更F7 src_bidchangef7 |
| 3 | fnewbidname | 招标项目名称(变更后) | varchar | 300 |  | √ | ' ' | 招标项目名称(变更后) |
| 4 | fprojectid | 寻源项目F7 | int8 | 64 |  | √ | 0 | 招标项目F7 src_projectf7 |
| 5 | fparentid | 父单据ID | varchar | 50 |  | √ | ' ' | 父单据ID |
| 6 | fchgsrcbillid | 变更源单ID | int8 | 64 |  | √ | 0 | 变更源单ID |
| 7 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | forgid | 主业务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fentitykey | 组件标识 | varchar | 50 |  | √ | ' ' | 组件标识 |
| 10 | fcompbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 11 | fpentitykey | 父单据标识 | varchar | 50 |  | √ | ' ' | 父单据标识 |
| 12 | fbidname | 招标项目名称(变更前) | varchar | 300 |  | √ | ' ' | 招标项目名称(变更前) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_projectinfochg_pid |  | fparentid |
| 2 | pk_src_projectinfochg |  | fid |
