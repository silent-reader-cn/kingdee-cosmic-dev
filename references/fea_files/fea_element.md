# 数据元素-fea_element

## 数据元素-多语言表 t_fea_element_l

- **表名称：** 数据元素-多语言表
- **表名：** t_fea_element_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fea_element_l |  | fid,flocaleid |
| 2 | pk_t_fea_element_l |  | fpkid |

---

## 数据元素-主表 t_fea_element

- **表名称：** 数据元素-主表
- **表名：** t_fea_element

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fdescription | 注释 | varchar | 255 |  | √ | ' ' | 注释 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | ftypeid | 数据类型 | int8 | 64 |  | √ | 0 | 数据类型 fea_datatype |
| 8 | fiscommon | 是否可被引用 | bpchar | 1 |  | √ | ' ' | 是否可被引用 |
| 9 | fstandardid | 文件标准 | int8 | 64 |  | √ | 0 | 文件标准 fea_standard |
| 10 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fassistitem | 辅助项 | bpchar | 1 |  | √ | '0' | 辅助项 |
| 14 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 15 | fnumber | 编码 | varchar | 255 |  | √ | ' ' | 编码 |
| 16 | fcount | 辅助项个数 | int8 | 64 |  | √ | 0 | 辅助项个数 |
| 17 | fnamefield1 |  | varchar | 50 |  | √ | ' ' |  |
| 18 | fnamefield2 |  | varchar | 50 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fea_element |  | fid |
| 2 | idx_fea_element |  | fstandardid |
