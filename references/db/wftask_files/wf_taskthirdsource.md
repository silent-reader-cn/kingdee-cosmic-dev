# 第三方来源数据-wf_taskthirdsource

## 第三方来源数据-多语言表 t_wf_taskthirdsource_l

- **表名称：** 第三方来源数据-多语言表
- **表名：** t_wf_taskthirdsource_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsysname | 系统名称 | varchar | 50 |  | √ | ' ' | 系统名称 |
| 3 | fbizname | 业务名称 | varchar | 50 |  | √ | ' ' | 业务名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_wf_taskthridsource_l |  | fpkid |
| 2 | idx_wf_taskthridsource_l |  | fid,flocaleid |

---

## 第三方来源数据-主表 t_wf_taskthirdsource

- **表名称：** 第三方来源数据-主表
- **表名：** t_wf_taskthirdsource

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreator | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | fsysnumber | 系统编码 | varchar | 50 |  | √ | ' ' | 系统编码 |
| 5 | fsysname | 系统名称 | varchar | 50 |  | √ | ' ' | 系统名称 |
| 6 | fbiznumber | 业务编码 | varchar | 50 |  | √ | ' ' | 业务编码 |
| 7 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fbizname | 业务名称 | varchar | 50 |  | √ | ' ' | 业务名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_wf_taskthridsource |  | fid |
| 2 | idx_wf_tasktrdsrc_biznumber |  | fbiznumber |
| 3 | idx_wf_tasktrdsrc_sysnumber |  | fsysnumber |
