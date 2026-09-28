# 本地内容-iprm_localcontent

## 本地内容-主表 t_iprm_localcontent

- **表名称：** 本地内容-主表
- **表名：** t_iprm_localcontent

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 简介 | varchar | 2000 |  | √ | ' ' | 简介 |
| 3 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 4 | fentryconfig | 子文件配置 | varchar | 2000 |  | √ | ' ' | 子文件配置 |
| 5 | fbillno | 编码 | varchar | 128 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_iprm_localcontent |  | fid |
| 2 | idx_iprm_localcontent_fbillno |  | fbillno |

---

## 本地内容-多语言表 t_iprm_localcontent_l

- **表名称：** 本地内容-多语言表
- **表名：** t_iprm_localcontent_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_iprm_localcontent_l_name |  | fname |
| 2 | pk_t_iprm_localcontent_l |  | fpkid |
