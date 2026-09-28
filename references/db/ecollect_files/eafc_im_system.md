# 集成系统-eafc_im_system

## 集成系统-多语言表 tk_eafc_im_system_l

- **表名称：** 集成系统-多语言表
- **表名：** tk_eafc_im_system_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 系统名称 | varchar | 50 |  | √ | ' ' | 系统名称 |
| 3 | flocaleid | flocaleid | varchar | 50 |  | √ | null | localeid |
| 4 | fpkid | fpkid | varchar | 50 |  | √ | null | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_eafc_im_system_l |  | fpkid |

---

## 集成系统-主表 tk_eafc_im_system

- **表名称：** 集成系统-主表
- **表名：** tk_eafc_im_system

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fk_eafc_port | 端口 | int8 | 64 |  |  | null | 端口 |
| 4 | fname | fname | varchar | 50 |  |  | null |  |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fk_eafc_ip | 服务器IP或域名 | varchar | 50 |  | √ | ' ' | 服务器IP或域名 |
| 7 | fk_eafc_http_protocol | HTTP协议 | varchar | 50 |  | √ | ' ' | HTTP协议,枚举: 1 :http 2 :https |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  |  | null | 主数据内码 |
| 12 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 13 | fnumber | 系统编码 | varchar | 30 |  | √ | ' ' | 系统编码 |
| 14 | fk_eafc_desc | 系统描述 | varchar | 500 |  | √ | ' ' | 系统描述 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__eafc_im_system |  | fid |
