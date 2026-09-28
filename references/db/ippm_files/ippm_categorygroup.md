# 文件夹-ippm_categorygroup

## 文件夹-多语言表 t_ippm_categorygroup_l

- **表名称：** 文件夹-多语言表
- **表名：** t_ippm_categorygroup_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 文件夹名称 | varchar | 200 |  | √ | ' ' | 文件夹名称 |
| 3 | ffullname | 长名称 | varchar | 200 |  | √ | ' ' | 长名称 |
| 4 | flocaleid | flocaleid | varchar | 200 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 50 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ippm_categorygroup_l |  | fpkid |

---

## 文件夹-主表 t_ippm_categorygroup

- **表名称：** 文件夹-主表
- **表名：** t_ippm_categorygroup

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 文件夹名称 | varchar | 200 |  | √ | ' ' | 文件夹名称 |
| 3 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | flevel | 级次 | int8 | 64 |  | √ | 0 | 级次 |
| 6 | fisleaf | 是否叶子 | bpchar | 1 |  | √ | '1' | 是否叶子 |
| 7 | fparentid | 上级文件夹 | int8 | 64 |  | √ | 0 | [文件夹 ippm_categorygroup](../ippm_files/ippm_categorygroup.md) |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | flongnumber | 长编码 | varchar | 200 |  | √ | ' ' | 长编码 |
| 10 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 11 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ippm_categorygroup |  | fid |
