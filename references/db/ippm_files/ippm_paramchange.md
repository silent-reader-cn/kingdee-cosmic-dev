# 参数变动监控-ippm_paramchange

## 参数变动监控-主表 t_ippm_paramchange

- **表名称：** 参数变动监控-主表
- **表名：** t_ippm_paramchange

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 参数名称 | varchar | 50 |  | √ | ' ' | 参数名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fparamtype | 参数类型 | varchar | 50 |  | √ | ' ' | 参数类型,枚举: sys :系统参数 |
| 6 | fbeforevalue | 修改前 | varchar | 2000 |  | √ | ' ' | 修改前 |
| 7 | fparamlevel | 参数级别 | varchar | 50 |  | √ | ' ' | 参数级别,枚举: app :应用 system :系统 |
| 8 | fappid | 应用 | varchar | 50 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | faftervalue | 修改后 | varchar | 2000 |  | √ | ' ' | 修改后 |
| 11 | fcloudid | 领域 | varchar | 50 |  | √ | ' ' | [业务云 bos_devportal_bizcloud](../mdl_files/bos_devportal_bizcloud.md) |
| 12 | fviewtypeid | 职能类型 | int8 | 64 |  | √ | 0 | [组织职能类型 bos_org_biz](../base_files/bos_org_biz.md) |
| 13 | fmenupath | 菜单路径 | varchar | 200 |  | √ | ' ' | 菜单路径 |
| 14 | fclassification | 参数分类 | varchar | 200 |  | √ | ' ' | 参数分类 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ippm_paramchange |  | fid |
| 2 | idx_ippm_paramchange |  | fmodifytime |
