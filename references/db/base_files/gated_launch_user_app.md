# 灰度用户管理-gated_launch_user_app

## 人员-多选基础资料表 t_sec_gatedlaunchappuser

- **表名称：** 人员-多选基础资料表
- **表名：** t_sec_gatedlaunchappuser

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 3 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 4 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 7 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_sec_gatedlaunchappuser |  | fpkid |
| 2 | idx_sec_gatedlaunchappuser_fk |  | fid |

---

## 灰度用户管理-主表 t_sec_gatedlaunchapp

- **表名称：** 灰度用户管理-主表
- **表名：** t_sec_gatedlaunchapp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 3 | fappnumber | 应用编码 | varchar | 80 |  | √ | ' ' | 应用编码 |
| 4 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 5 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 6 | appid | appid | varchar | 50 |  |  | ' ' |  |
| 7 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 8 | fprodnum | displayprod | varchar | 50 |  |  | ' ' | displayprod |
| 9 | fappids | 应用id | varchar | 1024 |  | √ | ' ' | 应用id |
| 10 | fversion | 版本标识 | varchar | 50 |  | √ | ' ' | 版本标识 |
| 11 | fappid | fappid | varchar | 50 |  | √ | ' ' |  |
| 12 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_sec_gatedlaunchapp |  | fid |
| 2 | index_t_sec_gatedapp_version |  | fappnumber,fversion |

---

## 用户分组-多选基础资料表 t_sec_grayappusergroup

- **表名称：** 用户分组-多选基础资料表
- **表名：** t_sec_grayappusergroup

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 灰度用户分组 gray_user_group |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sec_grayappusergroup_fk |  | fid |
| 2 | pk_t_sec_grayappusergroup |  | fpkid |
