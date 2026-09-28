# 集成配置-rpap_config

## 集成配置-主表 t_rpap_config_setting

- **表名称：** 集成配置-主表
- **表名：** t_rpap_config_setting

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsecret | 对称加密秘钥 | varchar | 255 |  | √ | ' ' | 对称加密秘钥 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fappsecret | 应用Secret | varchar | 50 |  | √ | ' ' | 应用Secret |
| 5 | fthirdtypeid | 第三方类型 | int8 | 64 |  | √ | 0 | 第三方类型 rpap_thirdtype |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fappidset | 应用ID | varchar | 50 |  | √ | ' ' | 应用ID |
| 8 | fappid | 第三方应用 | int8 | 64 |  | √ | 0 | 第三方应用（废弃） open_3rdapps |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fenable | 是否启用 | varchar | 30 |  | √ | ' ' | 是否启用,枚举: 0 :停用 1 :启用 |
| 14 | fnumber | 编码 | varchar | 255 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_rpap_config_setting |  | fid |
| 2 | idx_rpap_config_setting_appid |  | fappid |

---

## 集成配置-多语言表 t_rpap_config_setting_l

- **表名称：** 集成配置-多语言表
- **表名：** t_rpap_config_setting_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 第三方应用名称 | varchar | 255 |  |  | ' ' | 第三方应用名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_config_setting_l_fid |  | fid |
| 2 | pk_t_rpap_config_setting_l |  | fpkid |
