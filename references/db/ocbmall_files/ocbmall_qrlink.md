# 首页二维码链接-ocbmall_qrlink

## 首页二维码链接-主表 t_ocbmall_qrlink

- **表名称：** 首页二维码链接-主表
- **表名：** t_ocbmall_qrlink

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fqrimg | 二维码图片 | varchar | 300 |  | √ | ' ' | 二维码图片 |
| 3 | fstatus | fstatus | bpchar | 1 |  | √ | ' ' |  |
| 4 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 7 | fqrurl | 要显示二维的链接 | varchar | 300 |  | √ | ' ' | 要显示二维的链接 |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | fportalscope | 所属门户首页 | varchar | 100 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 10 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 11 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 12 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocbmall_qrlink_enable |  | fenable |
| 2 | pk_ocbmall_qrlink |  | fid |

---

## 首页二维码链接-多语言表 t_ocbmall_qrlink_l

- **表名称：** 首页二维码链接-多语言表
- **表名：** t_ocbmall_qrlink_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocbmall_qrlink_l |  | fpkid |
| 2 | idx_ocbmall_qrlink_flid |  | fid,flocaleid |
