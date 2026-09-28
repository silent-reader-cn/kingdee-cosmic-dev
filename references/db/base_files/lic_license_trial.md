# 许可试算-lic_license_trial

## 许可试算-主表 t_lic_license_trial

- **表名称：** 许可试算-主表
- **表名：** t_lic_license_trial

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fproductversion | 产品版本 | varchar | 30 |  | √ | ' ' | 产品版本 |
| 3 | factivedate | 激活日期 | timestamp | 0 |  |  | null | 激活日期 |
| 4 | fname | 许可名称 | varchar | 255 |  | √ | ' ' | 许可名称 |
| 5 | fsoftwarecode | 软件特征码 | varchar | 50 |  | √ | ' ' | 软件特征码 |
| 6 | fscenetype | 场景 | varchar | 30 |  | √ | ' ' | 场景 |
| 7 | fexpdate | 过期日期 | timestamp | 0 |  |  | null | 过期日期 |
| 8 | fprodid | 所属产品 | varchar | 36 |  | √ | ' ' | [ISV产品 lic_isvprod](../base_files/lic_isvprod.md) |
| 9 | ftype | 类型 | varchar | 30 |  | √ | ' ' | 类型,枚举: 1 :正式许可 2 :临时许可 |
| 10 | fproductid | 产品ID | varchar | 50 |  | √ | ' ' | 产品ID |
| 11 | ftid | 客户唯一标识 | varchar | 255 |  | √ | ' ' | 客户唯一标识 |
| 12 | fproductno | 产品序列号 | varchar | 50 |  | √ | ' ' | 产品序列号 |
| 13 | findustry | 行业 | varchar | 30 |  | √ | ' ' | 行业 |
| 14 | fsoftwarename | 软件名称 | varchar | 255 |  | √ | ' ' | 软件名称 |
| 15 | fprodinstcode | 产品实例码 | varchar | 50 |  | √ | ' ' | 产品实例码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_lic_license_trial |  | fid |
| 2 | idx_lic_license_trial_pic |  | fprodinstcode |

---

## 许可分组明细-子表 t_lic_licdetail_trial

- **表名称：** 许可分组明细-子表
- **表名：** t_lic_licdetail_trial

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fgroupid | 许可分组 | int8 | 64 |  | √ | 0 | [许可分组 lic_group](../base_files/lic_group.md) |
| 3 | fenddate | 租赁结束日时间 | timestamp | 0 |  |  | null | 租赁结束日时间 |
| 4 | fassignedcount | 已分配数 | int4 | 32 |  | √ | 0 | 已分配数 |
| 5 | fremaincount | 剩余数 | int4 | 32 |  | √ | 0 | 剩余数 |
| 6 | fbegindate | 租赁起始时间 | timestamp | 0 |  |  | null | 租赁起始时间 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | ftotalcount | 总数 | int4 | 32 |  | √ | 0 | 总数 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_lic_licdetail_trial |  | fentryid |
| 2 | idx_lic_licdetail_trial_lic |  | fid |

---

## 许可分组应用-子表 t_lic_licgroupapps_trial

- **表名称：** 许可分组应用-子表
- **表名：** t_lic_licgroupapps_trial

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fmoduleenddate | 失效时间 | timestamp | 0 |  |  | null | 失效时间 |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 4 | fmodulebegindate | 生效时间 | timestamp | 0 |  |  | null | 生效时间 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 6 | fmoduleid | 已购买模块 | int8 | 64 |  | √ | 0 | [许可模块 lic_module](../base_files/lic_module.md) |
| 7 | fbizappid | 已购买应用 | varchar | 36 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_lic_licgroupapps_trial |  | fdetailid |
| 2 | idx_lic_licgroupapp_trial_ug |  | fentryid |
