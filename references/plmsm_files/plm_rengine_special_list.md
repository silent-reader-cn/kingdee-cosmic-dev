# 名单管理-plm_rengine_special_list

## 字符串-子表 t_plm_egn_list_string

- **表名称：** 字符串-子表
- **表名：** t_plm_egn_list_string

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fliststringname | 名单 | varchar | 255 |  | √ | ' ' | 名单 |
| 3 | findex | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fstringdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_list_string |  | fid,fliststringname |
| 2 | pk_plm_egn_list_string |  | fentryid |

---

## 行政组织-子表 t_plm_egn_list_org

- **表名称：** 行政组织-子表
- **表名：** t_plm_egn_list_org

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | findex | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fentityorgid | 组织名称 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_list_org |  | fid,fentityorgid |
| 2 | pk_plm_egn_list_org |  | fentryid |

---

## 人员-子表 t_plm_egn_list_person

- **表名称：** 人员-子表
- **表名：** t_plm_egn_list_person

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | findex | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fentitypersonid | 姓名 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_list_person |  | fid,fentitypersonid |
| 2 | pk_plm_egn_list_person |  | fentryid |

---

## 名单管理-多语言表 t_plm_egn_special_list_l

- **表名称：** 名单管理-多语言表
- **表名：** t_plm_egn_special_list_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名单名称 | varchar | 100 |  | √ | ' ' | 名单名称 |
| 3 | fsimplename | 简称 | varchar | 100 |  | √ | ' ' | 简称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fdescription | 名单描述 | varchar | 255 |  | √ | ' ' | 名单描述 |
| 6 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_egn_special_list_l |  | fpkid |
| 2 | idx_plm_special_list_l |  | fid,flocaleid |

---

## 名单管理-主表 t_plm_egn_special_list

- **表名称：** 名单管理-主表
- **表名：** t_plm_egn_special_list

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名单名称 | varchar | 100 |  | √ | ' ' | 名单名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | findex | 排序号 | int4 | 32 |  | √ | 0 | 排序号 |
| 6 | fapplicationscope | 适用范围 | varchar | 50 |  | √ | ' ' | 适用范围,枚举: share :全局共享 private :私有 scopeshare :管控范围内共享 |
| 7 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 8 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fdescription | 名单描述 | varchar | 255 |  | √ | ' ' | 名单描述 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 数据状态 | varchar | 2 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | flistnable | flistnable | varchar | 2 |  | √ | '1' |  |
| 15 | flistcategory | 名单类别 | varchar | 50 |  | √ | ' ' | 名单类别,枚举: haos_adminorghr :行政组织 bos_user :系统人员 hsas_personhr :计薪人员 |
| 16 | fsimplename | 简称 | varchar | 100 |  | √ | ' ' | 简称 |
| 17 | fenable | 使用状态 | varchar | 2 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 10 :待启用 |
| 18 | flisttype | 名单类型 | varchar | 50 |  | √ | ' ' | 名单类型,枚举: basedata :基础资料 string :字符串 |
| 19 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 20 | fissyspreset | 是否系统预置 | bpchar | 1 |  | √ | '0' | 是否系统预置 |
| 21 | fbuid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_special_list |  | fnumber,fname |
| 2 | pk_plm_egn_special_list |  | fid |
