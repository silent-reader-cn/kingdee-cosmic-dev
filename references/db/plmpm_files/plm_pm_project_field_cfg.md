# 柔性容器字段配置-plm_pm_project_field_cfg

## 字段配置-多语言表 t_plmpm_project_field_cfg_l

- **表名称：** 字段配置-多语言表
- **表名：** t_plmpm_project_field_cfg_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fnewname | 重命名 | varchar | 50 |  | √ | ' ' | 重命名 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plmpm_project_field_cfg_l |  | fpkid |
| 2 | idx_plmpm_field_cfg_l_0 |  | fentryid,flocaleid |

---

## 柔性容器字段配置-主表 t_plmpm_project_field

- **表名称：** 柔性容器字段配置-主表
- **表名：** t_plmpm_project_field

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plmpm_project_field |  | fid |
| 2 | idx_t_plmpm_project_field_id |  | fcreatetime |

---

## 字段配置-子表 t_plmpm_project_field_cfg

- **表名称：** 字段配置-子表
- **表名：** t_plmpm_project_field_cfg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fshow | 成果(输出)列表 | bpchar | 1 |  | √ | '0' | 成果(输出)列表 |
| 3 | fshowscope | 范围(输入)列表 | bpchar | 1 |  | √ | '1' | 范围(输入)列表 |
| 4 | ffieldname | 字段 | varchar | 50 |  | √ | ' ' | 字段 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fnewname | 重命名 | varchar | 50 |  | √ | ' ' | 重命名 |
| 7 | fspecific | 特有属性 | varchar | 50 |  | √ | '0' | 特有属性 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | ffieldkey | 标识 | varchar | 50 |  | √ | ' ' | 标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plmpm_project_field_cfg_fk |  | fid |
| 2 | pk_plmpm_project_field_cfg |  | fentryid |
