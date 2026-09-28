# 自定义组件-ysq_rpa_library

## 单据体-子表 tk_ysq_rpa_library_l

- **表名称：** 单据体-子表
- **表名：** tk_ysq_rpa_library_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fmodifydatefield | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | '0' | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | null | id |
| 5 | fmodifierfield | 修改人 | int8 | 64 |  |  | null | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx__ysq_rpa_library_l_fk |  | fid |
| 2 | pk_tk_ysq_rpa_library_l |  | fentryid |

---

## 自定义组件-主表 tk_ysq_rpa_library

- **表名称：** 自定义组件-主表
- **表名：** tk_ysq_rpa_library

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  |  | null | 人员 bos_user |
| 3 | fk_ysq_lib_menu | 菜单 | varchar | 50 |  |  | NULL | 菜单 |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 组织 | int8 | 64 |  |  | null | 业务单元 bos_org |
| 7 | fk_ysq_lib_size | 文件大小 | varchar | 50 |  |  | NULL | 文件大小 |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fk_ysq_lib_pro_change | proChange | varchar | 50 |  |  | NULL | proChange |
| 10 | fk_ysq_lib_ver | 工程版本 | varchar | 50 |  |  | NULL | 工程版本 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  |  | null | 人员 bos_user |
| 13 | fk_ysq_lib_show_name | 组件名称 | varchar | 50 |  |  | NULL | 组件名称 |
| 14 | fk_ysq_lib_desc | 描述 | varchar | 50 |  |  | NULL | 描述 |
| 15 | fk_ysq_lib_code | 工程编号 | varchar | 50 |  |  | NULL | 工程编号 |
| 16 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 17 | fauditorid | 审核人 | int8 | 64 |  |  | null | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tk_ysq_rpa_library |  | fid |
